import unittest
from exercises.day15 import Solution, Node


class Test(unittest.TestCase):
    def test(self):
        mylist = Solution()
        head = None
        for i in [2,3,4,1]:
            data = i
            head = mylist.insert(head, data)
        mylist.display(head);