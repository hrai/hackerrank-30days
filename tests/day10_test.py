import unittest
from exercises.day10 import longest_ones

class TestBasicChecks(unittest.TestCase):

    def test_is_none(self):
        assert longest_ones(0) == 0

    def test_is_not_none(self):
        assert longest_ones(3) == 2

