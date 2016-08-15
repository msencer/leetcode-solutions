'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
'''
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        shift = 0
        while m!=n:
            shift +=1
            m>>=1
            n>>=1
        return m<<shift

if __name__ == "__main__":
    assert 4 == Solution().rangeBitwiseAnd(5,7)