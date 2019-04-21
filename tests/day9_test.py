import unittest
from exercises.day9 import factorial

class TestBasicChecks(unittest.TestCase):

    def test_is_none(self):
        assert factorial(0) == 0

    def test_is_not_none(self):
        assert factorial(3) == 6

