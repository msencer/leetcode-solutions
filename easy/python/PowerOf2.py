'''
Given an integer, write a function to determine if it is a power of two.
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n&(n-1) == 0

if __name__ == "__main__":
    assert False == Solution().isPowerOfTwo(3)
    assert True == Solution().isPowerOfTwo(128)