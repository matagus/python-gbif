# -*- coding: UTF-8 -*-
import sys

from xml.dom.minidom import parseString

from restkit import Resource


class Result(object):
    """
    """

    def __init__(self, **kwargs):
        self.key = kwargs.get("key")
        self.primary = kwargs.get("primary")
        self.status = kwargs.get("status")
        self.fullname = kwargs.get("fullname")

    def __unicode__(self):
        return u"%s (%s) [%s]" % (self.fullname, self.__class__.__name__, self.status)

    def __repr__(self):
        return unicode(self)


class Kingdom(Result):
    """
    """
    pass


class Phylum(Result):
    """
    """
    pass


class Family(Result):
    """
    """
    pass


class Class(Result):
    """
    """
    pass


class Order(Result):
    """
    """
    pass


class Genus(Result):
    """
    """
    pass


class SubGenus(Result):
    """
    """
    pass


class Species(Result):
    """
    """
    pass


class Infraspecific(Result):
    """
    """
    pass


class Variety(Result):
    """
    """
    pass


class Form(Result):
    """
    """
    pass


class NothoSpecies(Result):
    """
    """
    pass


class SubSpecies(Result):
    """
    """
    pass


def result_factory(**kwargs):

    RANK_MAPPER = {
        "kingdom": Kingdom,
        "phylum": Phylum,
        "class": Class,
        "order": Order,
        "family": Family,
        "genus": Genus,
        "subgenus": SubGenus,
        "species": Species,
        "subspecies": SubSpecies,
        "infraspecific": Infraspecific,
        "variety": Variety,
        "form": Form,
        "nothospecies": NothoSpecies,
    }
    return RANK_MAPPER[kwargs.get("rank")](**kwargs)


class Client(Resource):

    def __init__(self, **kwargs):
        base_url = "http://data.gbif.org/ws/rest/taxon/"
        super(Client, self).__init__(
            base_url, follow_redirect=True, max_follow_redirect=10, **kwargs)

    def search(self, name, start=0, count=50):
        # TODO: add param
        # rank: kingdom, phylum, class, order, family, genus, species, infraspecific
        return self.get("/list/", scientificname=name, startindex=start,
            maxresults=count, stylesheet="")

    def get_by(self, key):
        if not isinstance(key, (int, log)):
            print "key param must be an integer number."
            return None

        return self.get("/key/%d/" % key, stylesheet="")

    def request(self, *args, **kwargs):
        resp = super(Client, self).request(*args, **kwargs)
        body = resp.body_string()
        dom = parseString(body)
        items = []
        concept_list = dom.getElementsByTagName("tc:TaxonConcept")
        for concept in concept_list:
            items.append(self._to_item(concept))
        return items

    def _to_item(self, xml_concept):
        key = xml_concept.getAttribute("gbifKey").encode("utf-8")
        status = xml_concept.getAttribute("status").encode("utf-8")
        primary = xml_concept.getElementsByTagName("tc:primary")[0].firstChild.nodeValue == "true"
        fullname = xml_concept.getElementsByTagName("tn:nameComplete")[0].firstChild.nodeValue.encode("utf-8")
        rank = xml_concept.getElementsByTagName("tn:rankString")[0].firstChild.nodeValue.encode("utf-8")

        return result_factory(key=key, primary=primary,
            fullname=fullname, status=status, rank=rank)

if __name__ == "__main__":
    if not sys.argv[1:]:
        print "Please provide a name to search for."
        exit(0)

    name = " ".join(sys.argv[1:])

    s = Client()
    print s.search(name)
