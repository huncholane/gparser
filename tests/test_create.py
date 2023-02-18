import parsers
import unittest


class Test(parsers.Parser):
    a = parsers.Field()


class TestCreate(unittest.TestCase):

    def test_create(self):
        t = Test('a')
        self.assertEqual(t.a, 'a')

    def test_nullable(self):
        pass
