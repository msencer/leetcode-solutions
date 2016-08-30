"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        strsCount = len(strs)
        if not strsCount:
            return ""
        if strsCount == 1:
            return strs[0]

        firstStringLength = len(strs[0])

        for j in xrange(firstStringLength):
            for i in xrange(strsCount - 1):
                if j >= len(strs[i + 1]) or strs[i][j] != strs[i + 1][j]:
                    if j == 0:
                        return ""
                    else:
                        return strs[i][:j]
        return strs[0]


if __name__ == "__main__":
    assert "ab" == Solution().longestCommonPrefix(["abcab","ab","abaads"])
    assert "" == Solution().longestCommonPrefix(["asdasd","ddsdd"])