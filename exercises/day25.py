
import math

class Solution:
    def is_prime(this, num):
        if num==2 or num==3:
            return True

        if num <2 or num % 2==0:
            return False

        for divisor in range(3, int(math.sqrt(num)+1), 2):
            if num %divisor==0:
                return False

        return True
