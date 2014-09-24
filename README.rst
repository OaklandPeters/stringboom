StringBoom
============


Synopsis
---------
String-related functions for (1) regex convenience functions, and (2) partial-application of string formatting/templates.

StringTemplate
---------------------
As an example of StringTemplate, for partially-applying str.format.

.. code:: python

	template = StringTemplate('DELETE FROM {table} WHERE {pkey} IN ({chunk})')
	result = template.format(table='import')
	# => 'DELETE FROM import WHERE {pkey} IN ({chunk})'
	result.format(pkey='id', chunk='1001, 1002')
	# => 'DELETE FROM import WHERE id IN (1001, 1002)'


Extended Regex
--------

Core regex functions (``re_iter``, ``re_find``, ``re_all``, and ``re_test``) act as simple convenience functions around standard python regex functionality (from ``re``).

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

They also provide support for a more functional-style of programming, via ``make``, which constructs partial-functions

.. code:: python

    assert re_find('a.', 'a aa bbbac') == make(re_find, 'a.')('a aa bbac')
    phrases = [
        'Nay, answer me: stand, and unfold yourself.',
        'Long live the king!',
        'You come most carefully upon your hour.',
        'I think I hear them. Stand, ho! Whos there?'
    ]
    re_filter = make(re_test, r'\bt\S*') # Does it contain a word begining with 't'?
    filter(re_filter, phrases)
    # => ['Long live the king!', 'I think I hear them. Stand, ho! Whos there?']

API
-------------
``re_iter``, ``re_find``, ``re_all``, and ``re_test`` have the following argument form::

    def re_function(regex, _string, flags=0):

* **regex:** raw-string or string. This is eventually passed to `re.compile(regex, flags) <https://docs.python.org/2/library/re.html#re.compile/>`_
* **_string:** the input string to be tested.
* **flags:** optional. See specification following `re.compile <https://docs.python.org/2/library/re.html#re.DEBUG/>`_

``make()`` is very simple, with the following structure::

	def make(re_function, regex, flags=0):
		return functools.partial(re_func, regex, flags=flags)
		
License (MIT)
-----------
Copyright (c) 2014, Oakland John Peters.