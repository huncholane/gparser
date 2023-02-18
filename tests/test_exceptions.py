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
    t2 = Test(a='a', b='b', c='c', d='d2')


class TestExceptions(unittest.TestCase):

    def test_unique(self):
        self.assertRaises(
            parsers.exceptions.UniqueFieldParseError, raise_unique_error)
