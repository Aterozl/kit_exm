from nose.tools import eq_, ok_
import unittest2

from app.reg import reg

class Event1TestCase(unittest2.TestCase):
    def test_str(self):
        eq_(reg('asd'), False)
    def test_str1(self):
        eq_(reg('123'), False)
    def test_str2(self):
        eq_(reg('asd123'), False)
    def test_str3(self):
        eq_(reg('192.168.0.0 bar.domain.tld'), "192.168.0.0 baz.donemain.tld")
