import unittest
import parsers
import datetime as dt


class FieldParser(parsers.Parser):
    a = parsers.Field()


class HourMinuteIntParser(parsers.Parser):
    a = parsers.HourMinuteIntField()


class HourMinuteDeltaParser(parsers.Parser):
    a = parsers.HourMinuteDeltaField()


class PhoneParser(parsers.Parser):
    a = parsers.PhoneField()


class StrParser(parsers.Parser):
    a = parsers.StrField()


class IntParser(parsers.Parser):
    a = parsers.IntField()


class FloatParser(parsers.Parser):
    a = parsers.FloatField()


class BoolParser(parsers.Parser):
    a = parsers.BooleanField()


class TestField(unittest.TestCase):
    cls = FieldParser
    good_vals = ['a']
    bad_vals = []
    type = str

    def test_good_vals(self):
        for val in self.good_vals:
            t = self.cls(a=val)
            self.assertEqual(type(t.a), self.type)

    def test_bad_vals(self):
        def func():
            self.cls(a=val)
        for val in self.bad_vals:
            self.assertRaises(Exception, func)


class TestHourMinuteDeltaField(TestField):
    cls = HourMinuteDeltaParser
    good_vals = ['23421', '23:32', '234:21', '2323'].copy()
    bad_vals = ['fds', '234', '3:3'].copy()
    type = dt.timedelta


class TestHourMinuteIntField(TestHourMinuteDeltaField):
    cls = HourMinuteIntParser
    type = int


class TestPhoneField(TestField):
    cls = PhoneParser
    good_vals = ['32452345', '232-234-234-']
    bad_vals = ['asedrfaw']

    def test_foreign(self):
        t = self.cls(a='011-123-456-789')
        self.assertEqual(t.a, '+123456789')

    def test_us(self):
        t = self.cls(a='123456789')
        self.assertEqual(t.a, '+1123456789')


class TestStrField(TestField):
    cls = StrParser
    good_vals = ['asdf']


class TestIntField(TestField):
    cls = IntParser
    good_vals = ['2314', '32']
    bad_vals = ['adsf']
    type = int


class TestFloatField(TestField):
    cls = FloatParser
    good_vals = ['223.23', '23']
    bad_vals = ['asdf']
    type = float
