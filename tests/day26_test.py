import unittest

from exercises.day26 import Solution


class Test(unittest.TestCase):
    def test(self):
        sol=Solution()
        res = sol.calc("9 6 2015", "6 6 2015")
        assert res==45

    def test2(self):
        sol = Solution()
        res = sol.calc("1 1 1", "8 8 8")
        assert res==0

    def test1(self):
        sol = Solution()

        res = sol.calc("24 12 1898", "18 9 1898")
        #print(res)
        assert res==1500



    def test3(self):
        sol = Solution()

        res = sol.calc(" 8 4 12 ", "1 1 1")
        #print(res)
        assert res==10000
