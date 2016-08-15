'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mul = 1
        if x<0:
            mul=-1
        result =0
        x = abs(x)
        while x:
            result=result*10+x%10
            x/=10
        return result*mul if -2147483647<result<2147483647 else 0

if __name__ == "__main__":
    assert 151413 == Solution().reverse(314151)
    assert 0 == Solution().reverse(1231241591859)