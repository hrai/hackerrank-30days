import unittest
from exercises.day11 import largest_sum


def get_arr():
    arr= [list(map(int, "-1 -1 0 -9 -2 -2".split())),
          list(map(int, "-2 -1 -6 -8 -2 -5".split())),
          list(map(int, "-1 -1 -1 -2 -3 -4".split())),
          list(map(int, "-1 -9 -2 -4 -4 -5".split())),
          list(map(int, "-7 -3 -3 -2 -9 -9".split())),
          list(map(int, "-1 -3 -1 -2 -4 -5".split()))]

    return arr


class TestBasicChecks(unittest.TestCase):

    def test_is_none(self):
        res=largest_sum(get_arr())
        assert res == -6

    # def test_is_not_none(self):
    #     assert longest_ones(3) == 2

