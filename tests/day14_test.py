import unittest
from exercises.day14 import Difference


class TestBasicChecks(unittest.TestCase):
    def test_max_diff(self):
        arr = [1, 2, 5]
        diff = Difference(arr)
        diff.computeDifference()
        assert diff.maximumDifference == 4
