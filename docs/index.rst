.. Fundraising Innovations Wiki documentation master file, created by
   sphinx-quickstart on Wed Apr 25 10:25:12 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   TODO: instruction case: I want to change format of a table/page
   TODO: update everything


***************************
fundingwiki documentation
***************************

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   development

The aim of this package is to provide a two-way connection between
Innovations in Fundraising Wiki_ and an Airtable database.
The database stores part of the content that is published on the Wiki: mostly structured content such as evidence for
particular innovation tools and bibliographic references. The package provides a way to access this content in the
database and post it to the Wiki in various formats, i.e. as tables, pages or forms that can be filled in by users that
wish to contribute.

Currently only the database-to-wiki connection is implemented. That is, all the changes to the database-driven content
need to be done inside the database and then pushed to the wiki. (However, the wiki also links several Airtable forms enabling contributions/suggestions). In the future we may implement a wiki-to-database
connection that would allow content from the wiki to be pushed to the database.

.. _Wiki: http://innovationsinfundraising.org/doku.php


Features
---------

- Create new tables and pages on the wiki based on the database content
- Update existing wiki tables and pages based on changes to the database content


Modules
--------

:py:mod:`main`
:py:mod:`wikimanager`
:py:mod:`wikicontents`


Contribute
-----------

- Issue Tracker: https://github.com/kabramova/fundingwiki/issues
- Source Code: https://github.com/kabramova/fundingwiki

Support
--------

If you are having issues, please let us know in the Issue Tracker.


License
--------

The project is licensed under the BSD license.


Indices and tables
-------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
