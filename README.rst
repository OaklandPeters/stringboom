

StringBoom
============


Synopsis
--------
String-related functions for (1) regex convenience functions, and (2) partial-application of string formatting/templates.

Code Example
------------
As an example of Template(), for partially-applying str.format():

.. code:: python

	Template('DELETE FROM {table} WHERE {pkey} IN ({chunk})').format(table='import')
	
	'DELETE FROM import WHERE {pkey} IN ({chunk})'




~~BEWARE~~
===================================
Everything below is un-filled-in template-boilerplate.

==============================

@todo: Add in examples from regex.py

Motivation
-----------
A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

Installation
------------
Provide code examples and explanations of how to get the project.

API Reference
-------------
Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.

Tests
-----------
Describe and show how to run the tests with code examples.

Contributors
------------
Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.

License
-----------
A short snippet describing the license (MIT, Apache, etc.)


Actual Attribution
--------------------
This template was based on a `README.md <https://gist.github.com/jxson/1784669/>`_ by `Jason Campbell <https://gist.github.com/jxson/>`_ on Github.

For more information on ReStructuredText (RST) formatting, see the `QuickRef <http://docutils.sourceforge.net/docs/user/rst/quickref.html/>`_ and the useful online RST editor/linter at http://rst.ninjs.org/.