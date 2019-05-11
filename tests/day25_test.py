import unittest

from exercises.day25 import Solution


class Test(unittest.TestCase):
    def test(self):
        sol=Solution()

        for num in [2,3,5,17,907]:
            res = sol.is_prime(num)
            assert res==True

    def test2(self):
        sol = Solution()

        for num in [0,1,4,9,15]:
            res = sol.is_prime(num)
            assert res == False

    def test1(self):
        sol = Solution()

        for num in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484,
                529, 576, 625, 676, 729, 784, 841, 907]:
            res = sol.is_prime(num)
            assert res == False
