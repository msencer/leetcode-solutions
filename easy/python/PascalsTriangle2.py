'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
'''
import operator as op


class Solution(object):
    def comb(self, n, r):
        r = min(r, n - r)
        if r == 0: return 1
        numer = reduce(op.mul, xrange(n, n - r, -1))
        denom = reduce(op.mul, xrange(1, r + 1))
        return numer // denom

    def getRow(self, rowIndex):
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        return [self.comb(rowIndex, r) for r in xrange(0, rowIndex + 1)]

if __name__ == "__main__":
    assert [1,4,6,4,1] == Solution().getRow(4)