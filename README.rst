MD-Environ
==========

This is an extension to
`Python-Markdown <https://pythonhosted.org/Markdown/>`__ which allows
environment variables to be inserted into the text. I originally wrote
it for my `FORD <https://github.com/cmacmackin/ford>`__ Fortran
auto-documentation generator.

Installation
------------

This module can now be installed using ``pip``.

::

    pip install md-environ

Usage
-----

This module can be used in a program in the following way:

.. code:: python

    import markdown
    html = markdown.markdown(source, extensions=['md_environ.environ])

The syntax for use within your Markdown files is
``${ENVIRONMENT_VARIABLE}``. This statement will be replaced by the
contents of ``ENVIRONMENT_VARIABLE``, if it is defined, or by an empty
string otherwise.

ChangeLog
---------

Version 0.1
~~~~~~~~~~~

Initial release.
