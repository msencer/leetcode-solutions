'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''
class Solution(object):
    def trailingZeroes(self, n):
        res = 0
        i = 5
        while n/i:
            res+=n/i
            i*=5
        return res

if __name__ == "__main__":
    assert 24 == Solution().trailingZeroes(100)