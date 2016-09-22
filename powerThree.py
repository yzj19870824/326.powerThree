__author__ = 'jerry'

import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        maxPower = math.pow(3,(int)(math.log(0x7fffffff)/math.log(3)))
        if(maxPower % n == 0):
            return True
        else:
            return False


if __name__ == "__main__":
    n = 0
    so = Solution()
    print(so.isPowerOfThree(n))
