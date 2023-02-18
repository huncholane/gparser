from .exceptions import *
from .fields import Field


class Manager:

    def __init__(self):
        self.objects = []

    def set_cls(self, cls):
        """The Parser object tells the manager to use it"""
        self.cls = cls

    def create(self, **kwargs):
        """Create and save object"""
        cls = self.cls
        obj = cls(**kwargs)
        self.append(obj)

    def all(self):
        return self.objects

    def append(self, obj):
        self.objects.append(obj)

    def count(self):
        return len(self.objects)

    def exists(self, **kwargs):
        cls = self.cls
        newobj = cls(**kwargs)
        for obj in self.objects:
            if obj == newobj:
                return True
        return False

    def raise_unique_constraints(self, **kwargs):
        o2 = self.cls(**kwargs)
        unique_fields = [key for key, val in o2.field_items() if val.unique]
        unique_together = o2.Meta.unique_together
        for o in self.objects:
            for key in unique_fields:
                if o[key] == o2[key]:
                    raise UniqueFieldParseError(self.cls, key, o[key])
            unique_together_violation = True
            vals = []
            for key in unique_together:
                if o[key] != o2[key]:
                    unique_together_violation = False
                    break
                else:
                    vals.append(o[key])
            if unique_together_violation:
                raise UniqueTogetherParseError(self.cls, unique_together, vals)
