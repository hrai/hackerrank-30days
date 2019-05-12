import unittest
from exercises.day29 import bit_and_oper


class TestBasicChecks(unittest.TestCase):

    def test(self):
        resp = bit_and_oper(5, 2)
        assert resp == 1

    def test1(self):
        resp = bit_and_oper(8,5)
        assert resp == 4

    def test2(self):
        resp = bit_and_oper(2,2)
        assert resp == 0

    def test3(self):
        resp = bit_and_oper(9,2)
        assert resp == 1

    def test4(self):
        resp = bit_and_oper(8,3)
        assert resp == 2

