StringBoom
============


Synopsis
---------
String-related functions for (1) regex convenience functions, and (2) partial-application of string formatting/templates.

Code Example
-------------
As an example of Template(), for partially-applying str.format().

.. code:: python

	Template('DELETE FROM {table} WHERE {pkey} IN ({chunk})').format(table='import')
	# => 'DELETE FROM import WHERE {pkey} IN ({chunk})'

Regex functions act as simple convenience functions around core regex functions.

.. code:: python
	re_find('a.', 'a aa bbbac')		# 'a '
	re_find('E', 'a aa bbbac')		# Not found --> returns None
	
	# All standard regex syntax applies:
	re_find('^a', 'a aa bbbac')		# 'a'
	re_find('a$', 'a aa bbbac')		# Not found --> returns None
	
	re_all('a.', 'a aa bbbac')		# ['a ', 'aa', 'ac']
	
	re_test('^a', 'a aa bbbac')		# True
	re_test('a$', 'a aa bbbac')		# False

	for elm in re_iter('..', 'a aa bbbac'):
		print(elm)
	# a 
	# aa
	# b
	# bb
	# ac
