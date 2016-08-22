"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution(object):
    def firstUniqChar(self, s):
        charCounts = [0] * 26
        base = ord("a")
        for c in s:
            charCounts[ord(c) - base] += 1
        for i, v in enumerate(s):
            if charCounts[ord(v) - base] == 1:
                return i
        return -1

if __name__ == "__main__":
    assert 0 == Solution().firstUniqChar("leetcode")
    assert 2 == Solution().firstUniqChar("loveleetcode")