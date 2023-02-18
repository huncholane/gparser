import parsers
import unittest


class Test(parsers.Parser):
    a = parsers.Field()
    b = parsers.Field()
    c = parsers.Field()
    d = parsers.Field(unique=True)

    class Meta:
        unique_together = ['a', 'b', 'c']


def raise_unique_error():
    t1 = Test(a='a1', b='b1', c='c1', d='d')
    t1.save()
    t2 = Test(a='a2', b='b2', c='c2', d='d')
    t2.save()


def raise_unique_together():
    t1 = Test(a='a', b='b', c='c', d='d1')
    t1.save()
    t2 = Test(a='a', b='b', c='c', d='d2')
    t2.save()


def raise_missing_keys():
    Test(a='sdf')


def raise_extra_fields():
    Test(a='asdf', b='b', c='c', d='d', e='e')


def raise_with_id():
    Test(id='1', a='a', b='b', c='c', d='d')


class TestExceptions(unittest.TestCase):

    def test_unique(self):
        self.assertRaises(
            parsers.exceptions.UniqueFieldParseError, raise_unique_error)

    def test_unique_together(self):
        self.assertRaises(parsers.UniqueTogetherParseError,
                          raise_unique_together)

    def test_missing_keys(self):
        self.assertRaises(parsers.MissingFieldsParseError, raise_missing_keys)

    def test_extra_fields(self):
        self.assertRaises(parsers.ExtraFieldsParseError, raise_extra_fields)

    def test_with_id(self):
        self.assertRaises(parsers.CreateWithIdParseError, raise_with_id)
