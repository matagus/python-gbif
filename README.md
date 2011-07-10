Gbif API client
===============

A simple and pythonic client for Gbif Taxon Webservice. Pretty much work in progress.
See [Gbif Taxon Webservice API](http://data.gbif.org/ws/rest/taxon) for details.


OVERVIEW:
---------

This is the way to use it:

    >>> from gbif import Client
    >>> c = Client()
    >>> taxon = client.get_by(key=5661746)
    <Genus Orchid key=5661746 status='unconfirmed'>
    >>> taxon.key
    5661746
    >>> taxon.url
    'http://data.gbif.org/ws/rest/taxon/get/5661746/'
    >>> taxon.fullname
    'Orchid'
    >>> taxon.status
    'unconfirmed'
    >>> taxon.primary
    True
    >>> # searching by scientific name and rank
    >>> c.search("Cymbidium")
    [<Genus Cymbidium key=16286243 status=unconfirmed>, <Genus Cymbidium key=16308408 status=unconfirmed>,
    <Genus Cymbidium key=14751259 status=accepted>, <SubGenus Cymbidium key=16069947 status=unconfirmed>]
    >>> c.search("Cymbidium", rank="subgenus")
    [<SubGenus Cymbidium key=6313072 status=unconfirmed>, <SubGenus Cymbidium key=7843799 status=unconfirmed>,
    <SubGenus Cymbidium key=7926640 status=unconfirmed>, <SubGenus Cymbidium key=16069947 status=unconfirmed>,
    <SubGenus Cymbidium key=7709563 status=unconfirmed>, <SubGenus Cymbidium key=17001172 status=unconfirmed>, 
    <SubGenus Cymbidium key=7033101 status=unconfirmed>]
    >>> c.search("Cymbidium", rank="genus")
    [<Genus Cymbidium key=16286243 status=unconfirmed>, <Genus Cymbidium key=16308408 status=unconfirmed>,
    <Genus Cymbidium key=14751259 status=accepted>]
    >>> c.search("Cymbidium", rank="species")
    []
    >>> c.search("aerides", rank="genus")
    [<Genus Aerides key=14750373 status=accepted>]
    >>> c.search("orchid", rank="genus")
    [<Genus Orchid key=5661746 status=unconfirmed>, <Genus Orchid key=16409837 status=unconfirmed>,
    <Genus Orchid key=23768848 status=unconfirmed>]
    >>> c.search("cattleya", rank="genus")
    [<Genus Cattleya key=13232033 status=accepted>]
    >>> c.search("Dendrobium", rank="genus")
    [<Genus Dendrobium key=13232902 status=accepted>]
    >>> c.search("Dendrobium", rank="species")
    []
    >>> c.search("Dendrobium", rank="subgenus")
    [<SubGenus Dendrobium key=7927123 status=unconfirmed>, <SubGenus Dendrobium key=16133082 status=unconfirmed>, 
    <SubGenus Dendrobium key=6417149 status=unconfirmed>, <SubGenus Dendrobium key=6525783 status=unconfirmed>, 
    <SubGenus Dendrobium key=17000374 status=unconfirmed>, <SubGenus Dendrobium key=7035708 status=unconfirmed>]

REQUIREMENTS:
-------------

Please before using, install [restkit](http://benoitc.github.com/restkit/)
