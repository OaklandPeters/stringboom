StringBoom
============


Synopsis
---------
String-related functions for (1) regex convenience functions, and (2) partial-application of string formatting/templates.

Code Example
-------------
As an example of StringTemplate, for partially-applying str.format.

. code:: python

	StringTemplate('DELETE FROM {table} WHERE {pkey} IN ({chunk})').format(table='import')
	# => 'DELETE FROM import WHERE {pkey} IN ({chunk})'

Regex functions act as simple convenience functions around core regex functions.

. code:: python

	re_find('a.', 'a aa bbbac')
	re_find('E', 'a aa bbbac')