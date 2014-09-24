StringBoom
============


Synopsis
---------
String-related functions for (1) regex convenience functions, and (2) partial-application of string formatting/templates.


API
-------------
``re_iter``, ``re_find``, ``re_all``, and ``re_test`` have the following argument form:
	def re_function(regex, _string, flags=0):

Where:	
	regex: raw-string or string. This is eventually passed to `re.compile(regex, flags) <https://docs.python.org/2/library/re.html#re.compile/>`_
	_string: the input string to be tested
	flags: optional. See specification following `re.compile <https://docs.python.org/2/library/re.html#re.DEBUG/>`_

``make()`` is very simple, with the following structure:

.. code:: python
	def make(re_function, regex, flags=0):
		return functools.partial(re_func, regex, flags=flags)
		
License (MIT)
-----------
Copyright (c) 2014, Oakland John Peters.