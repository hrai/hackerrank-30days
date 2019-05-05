import unittest

from exercises.day22 import Solution


class Test(unittest.TestCase):
    def test(self):
        myTree = Solution()
        root = None
        treeData = [20, 50, 35, 44, 9, 15, 62, 11, 13]
        for i in treeData:
            data = i
            root = myTree.insert(root, data)


        height = myTree.getHeight(root)
        print(height)
        assert height == 4
