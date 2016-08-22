"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        pttr = list(pattern)
        string = str.split()
        lPttr = len(pttr)
        lStr = len(string)
        if lPttr != lStr or (not lStr):
            return False

        matcherPtr = {}
        matcherStr = {}
        for p, s in zip(pttr, string):
            if p in matcherPtr and matcherPtr[p] != s:
                return False
            elif s in matcherStr and matcherStr[s] != p:
                return False
            matcherPtr[p] = s
            matcherStr[s] = p
        return True

if __name__ == "__main__":
    assert True == Solution().wordPattern("aabb","cat cat dog dog")
    assert False == Solution().wordPattern("aa","dog cat")
    assert False == Solution().wordPattern("abba","dog dog dog dog")
    assert True == Solution().wordPattern("bc","b c")