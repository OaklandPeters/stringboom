from __future__ import absolute_import
import unittest

from stringboom.template import *





class StringTemplateTests(unittest.TestCase):
    def setUp(self):
        self.raw = 'DELETE FROM {table} WHERE {pkey} IN ({chunk})'
        self.complete = 'DELETE FROM temp_import WHERE id IN (1001, 1002, 1003)'
        self.template = StringTemplate(self.raw)
        self.keywords = {
            'table': 'temp_import',
            'pkey': 'id',
            'chunk': '1001, 1002, 1003'
        }

        
    def test_template_typecheck(self):
        format_result = self.template.format(table='temp_import')
        vformat_result = self.template.vformat((), self.keywords)
        
        self.assertEqual(type(self.template), StringTemplate)
        self.assert_(isinstance(self.template, StringTemplate))
        self.assert_(isinstance(self.template, str))
        self.assert_(isinstance(self.template, basestring))
        
        self.assertEqual(type(format_result), StringTemplate)
        self.assert_(isinstance(format_result, StringTemplate))
        self.assert_(isinstance(format_result, str))
        self.assert_(isinstance(format_result, basestring))
    
        self.assertEqual(type(vformat_result), str)
        self.assert_(not isinstance(vformat_result, StringTemplate))
        self.assert_(isinstance(vformat_result, str))
        self.assert_(isinstance(vformat_result, basestring))
    def test_vformat(self):
        # vformat does not support partial-formatting
        self.assertRaises(KeyError,
            lambda: self.template.vformat((), {'table': 'temp_import'})
        )
        
        self.assertEqual(
            self.template.vformat( (), self.keywords),
            self.complete
        )
        self.assertEqual(
            self.template.vformat((), self.keywords),
            self.template.format(**self.keywords)
        )
    
    def test_format(self):
        self.assertEqual(
            self.template.format(table='temp_import'),
            'DELETE FROM temp_import WHERE {pkey} IN ({chunk})'
        )
        self.assertEqual(
            self.template,
            self.raw
        )
        self.assertEqual(
            self.template.format(
                table='temp_import', pkey='id', chunk='1001, 1002, 1003'
            ),
            self.complete
        )
    def test_unpacking(self):
        self.assertEqual(
            self.template.format(**self.keywords),
            self.complete
        )
    def test_nonbindingmethod(self):
        self.assertEquals(
            StringTemplate.format(self.raw, **self.keywords),
            self.complete
        )
        self.assertEquals(
            StringTemplate.vformat(self.raw, (), self.keywords),
            self.complete
        )
    def test_positionals(self):
        self.assertEquals(
            StringTemplate("{0} went to the {1}").format('John'),
            'John went to the {1}'
        )
        self.assertEquals(
            StringTemplate("{0} went to the {1}").format('John', 'store'),
            'John went to the store'
        )
        self.assertEquals(
            StringTemplate("{0} went to the {1}").format(*['John', 'store']),
            'John went to the store'
        )


if __name__ == "__main__":
    unittest.main()