Gbif API client
===============

A simple and pythonic client for Gbif Taxon Webservice.
See [this](http://data.gbif.org/ws/rest/taxon) for details.


OVERVIEW:
---------

This is the way to use it:

    >>> from gbif import Client
    >>> c = Client()
    >>> l = c.search("Aerides")
    >>> l
    [Aerides (Genus) [accepted], Aerides (SubGenus) [unconfirmed]]
    >>> for r in l:
    ...     print r
    ... 
    Aerides (Genus) [accepted]
    Aerides (SubGenus) [unconfirmed]
    >>> r
    Aerides (SubGenus) [unconfirmed]
    >>> r.fullname
    'Aerides'
    >>> r.status
    'unconfirmed'
    >>> r.primary
    True
    >>> r.key
    '16070715'


REQUIREMENTS:
-------------

Please before using, install [restkit](http://benoitc.github.com/restkit/)


TODO:
-----

    * modularize it
    * add full unicode support
    * add Exceptions handling and raising
    * add caching support

    * little docs
    * test suite

    * Client:
        * get_by(key)
        * __len__: use API count method
        * search(...): make it lazy, use iterator in chunks to retrive the whole results.

    * setup.py, register & upload to pypi
