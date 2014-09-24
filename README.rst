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
