'''
Determine whether an integer is a palindrome. Do this without extra space.
'''

import math
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:  # negative numbers
            return False
        if x == 0:
            return True

        numberOfDigits = int(math.log(x, 10))
        divisor = 10 ** numberOfDigits
        while x:
            l, r = x // divisor, x % 10

            if l != r:
                return False

            x = (x % divisor) / 10
            divisor //= 100
        return True


if __name__ == "__main__":
    s = Solution()
    assert True     == s.isPalindrome(1)
    assert False    == s.isPalindrome(-1221)
    assert False    == s.isPalindrome(12211)
    assert True     == s.isPalindrome(1221)
    assert True     == s.isPalindrome(12321)