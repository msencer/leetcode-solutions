'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''
class Solution(object):
    def titleToNumber(self, s):
        l = len(s)
        res = 0
        for i in xrange(l-1,-1,-1):
            res += (ord(s[i]) - 64) * 26**(l-i-1)
        return res

if __name__ == "__main__":
    assert 28 == Solution().titleToNumber("AB")
    assert 26 == Solution().titleToNumber("Z")