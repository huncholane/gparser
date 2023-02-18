import parsers
import unittest


class TestCreate(unittest.TestCase):

    def test_create(self):
        class Test(parsers.Parser):
            a = parsers.Field()
        t = Test(a='a')
        self.assertEqual(t.a, 'a')

    def test_nullable(self):
        class Test(parsers.Parser):
            a = parsers.Field(null=True)
            b = parsers.Field()
        t = Test(b='32')
        self.assertEqual(t.a, None)
        self.assertEqual(t.b, '32')

    def test_default(self):
        class Test(parsers.Parser):
            a = parsers.Field(default='sdff')
            b = parsers.Field()
        t = Test(b='f')
        self.assertEqual(t.a, 'sdff')
        self.assertEqual(t.b, 'f')
