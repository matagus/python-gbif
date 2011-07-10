# -*- coding: UTF-8 -*-

class Result(object):
    """
    """

    def __init__(self, **kwargs):
        self.key = kwargs.get("key")
        self.url = kwargs.get("url")
        self.primary = kwargs.get("primary")
        self.status = kwargs.get("status")
        self.fullname = kwargs.get("fullname")
        self.parent = kwargs.get("parent")
        self._childs = None

    def __unicode__(self):
        return self.fullname

    def __str__(self):
        return u"<%s %s key=%s status=%s>" % (self.__class__.__name__,
            self.fullname.encode("utf-8", "ignore"), self.key, self.status)

    def __repr__(self):
        return str(self)

    @staticmethod
    def build_instance(**kwargs):
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
