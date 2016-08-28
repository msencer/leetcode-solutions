"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        hLen = len(haystack)
        nLen = len(needle)
        if nLen > hLen:
            return -1;
        if nLen == hLen == 0:
            return 0
        needleHash = hash(needle)
        for i in range(0,hLen-nLen+1):
            currentHash = hash(haystack[i:i+nLen])
            if currentHash == needleHash:
                return i
        return -1

if __name__ == "__main__":
    assert 7 == Solution().strStr("watermellon", "llon")
    assert 0 == Solution().strStr("","")
    assert -1 == Solution().strStr("I am Mehmet","ahmet")