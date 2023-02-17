from .manager import Manager
from .fields import Field, IntField
from .exceptions import *


class Parser:
    id = IntField()
    objects = Manager()

    class Meta:
        unique_together = []

    def __init__(self, **kwargs):
        self.objects.set_cls(type(self))
        missing_fields = set(self.fields())-set(kwargs)
        if 'id' not in missing_fields:
            raise CreateWithIdParseError(self)
        missing_fields = missing_fields-{'id'}
        if missing_fields:
            raise MissingFieldsParseError(self, missing_fields)
        extra_fields = set(kwargs)-set(self.fields())
        if extra_fields:
            raise ExtraFieldsParseError(self, extra_fields)
        kwargs['id'] = self.objects.count()
        for name, field in self.field_items():
            setattr(self, name, field.convert(kwargs[name]))

    def save(self):
        self.objects.append(self)

    def fields(self):
        """Gets the fields for the current object"""
        fields = {}
        for attr in dir(self):
            item = getattr(self, attr)
            if issubclass(type(item), Field):
                fields[attr] = item
        return fields

    def field_items(self):
        """Returns key value pairs for fields"""
        return self.fields().items()

    def __eq__(self, obj):
        matched = {key: False for key in set(self.__dict__)-{'id'}}
        for key in matched:
            if self.__dict__[key] == obj.__dict__[key]:
                return True
        return False not in matched.values()
