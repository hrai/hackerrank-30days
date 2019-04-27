class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        minnum = min(self.__elements)
        maxnum = max(self.__elements)

        self.maximumDifference = abs(maxnum - minnum)


