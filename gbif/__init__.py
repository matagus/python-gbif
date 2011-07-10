# -*- coding: UTF-8 -*-
"Basic and experimental Gbif Taxon API library for Python"
VERSION = (0, 1, 0)

__author__ = "Matías Agustín Méndez"
__contact__ = "matagus@gmail.com"
__homepage__ = "http://github.com/matagus/python-gbif"
__version__ = ".".join(map(str, VERSION))

import sys

from urlparse import urljoin
from xml.dom.minidom import parseString

from restkit import Resource

from gbif.models import Result


class Client(Resource):

    def __init__(self, **kwargs):
        self.base_url = "http://data.gbif.org/ws/rest/taxon/"
        super(Client, self).__init__(self.base_url,
            follow_redirect=True, max_follow_redirect=10, **kwargs)

    def search(self, name, rank=None, start=0, count=50):
        kwargs = dict(scientificname=name, startindex=start,
            maxresults=count, stylesheet="")

        if rank:
            kwargs.update(rank=rank)

        return self.get("/list/", **kwargs)

    def get_by(self, key):
        if not isinstance(key, (int, long)):
            raise TypeError("Key param must be an integer number")

        path = "/get/%d/" % key
        result_list = self.get(path, stylesheet="")
        primary_taxon = None
        for taxon in result_list:
            if taxon.primary:
                primary_taxon = taxon

        primary_taxon.url = urljoin(self.base_url, path)
        return primary_taxon

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
        key = long(xml_concept.getAttribute("gbifKey"))
        status = xml_concept.getAttribute("status")
        primary = xml_concept.getElementsByTagName("tc:primary")[0].firstChild.nodeValue == "true"
        fullname = xml_concept.getElementsByTagName("tn:nameComplete")[0].firstChild.nodeValue
        rank = xml_concept.getElementsByTagName("tn:rankString")[0].firstChild.nodeValue

        return Result.build_instance(key=key, primary=primary,
            fullname=fullname, status=status, rank=rank)

if __name__ == "__main__":
    if not sys.argv[1:]:
        print "Please provide a name to search for."
        exit(0)

    name = " ".join(sys.argv[1:])

    s = Client()
    print s.search(name)
