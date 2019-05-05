import unittest
from exercises.day20 import BubbleSort


class Test(unittest.TestCase):
    def test(self):
        sorter=BubbleSort()
        a=[2,3,4,1]
        n=len(a)

        totalsorts = sorter.sort(n,a)
        assert 7 == totalsorts

    def test_3_items(self):
        sorter=BubbleSort()
        a=[3,2,1]
        n=len(a)

        totalsorts = sorter.sort(n,a)
        assert 3 == totalsorts
