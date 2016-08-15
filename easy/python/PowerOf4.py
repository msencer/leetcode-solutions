'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.
'''
class Solution(object):
    def isPowerOfFour(self, num):
        if num == 1: return True
        if num < 4: return False

        f = False
        i = 0
        while num:
            if num & 1:
                if i % 2 or f:
                    return False
                f = True
            num >>= 1
            i += 1
        return f

if __name__ == "__main__":
    assert True == Solution().isPowerOfFour(64)
    assert False == Solution().isPowerOfFour(25)