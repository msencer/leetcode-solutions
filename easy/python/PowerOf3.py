'''
Given an integer, write a function to determine if it is a power of three.
'''
import math
class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0 :return False
        return n == 3 ** math.ceil(math.log(n,3))

if __name__ == "__main__":
    assert True == Solution().isPowerOfThree(27)
    assert False == Solution().isPowerOfThree(24)