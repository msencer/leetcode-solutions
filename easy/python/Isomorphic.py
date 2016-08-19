'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length
'''


class Solution(object):

    def isIsomorphic(self, s, t):
        if not s and not t:
            return True
        if not s:
            return False

        return self.__isoHelper(s, t) and self.__isoHelper(t, s)

    def __isoHelper(self, s, t):
        mappings = {}

        for c1, c2 in zip(s, t):
            if c2 in mappings and mappings[c2] != c1:
                return False
            mappings[c2] = c1

        return True

if __name__ == "__main__":
    assert True == Solution().isIsomorphic("foo","add")
    assert False == Solution().isIsomorphic("aa", "ab")
    assert True == Solution().isIsomorphic("ab", "ba")