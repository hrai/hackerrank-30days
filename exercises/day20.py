class BubbleSort(object):
    """Docstring for BubbleSort. """

    def __init__(self):
        """TODO: to be defined1. """


    def sort(self, n, a):
        totalSwaps = 0

        for i in range(0, n):
            swaps = 0

            for j in range(0, n - 1):
                if a[j] > a[j + 1]:
                    a[j+1], a[j] = a[j], a[j+1]
                    swaps += 1

            totalSwaps += swaps

            if swaps == 0:
                break

        return totalSwaps
