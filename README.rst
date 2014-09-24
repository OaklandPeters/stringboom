StringBoom
============


Synopsis
---------
String-related functions for (1) regex convenience functions, and (2) partial-application of string formatting/templates.

Code Example
-------------
As an example of StringTemplate, for partially-applying str.format.

.. code:: python

	StringTemplate('DELETE FROM {table} WHERE {pkey} IN ({chunk})').format(table='import')
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

They also provide support for a more functional-style of programming, via ``make``, which constructs partial-functions:

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
