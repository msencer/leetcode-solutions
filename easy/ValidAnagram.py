'''
Given two strings s and t, write a function to determine if t is an anagram of s.
'''
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        arr = [0]*256
        for c in s:
            arr[ord(c)]+=1
        for c in t:
            arr[ord(c)]-=1
        return all([x==0 for x in arr])


s = Solution()
assert True == s.isAnagram("","")
assert False == s.isAnagram("var","car")
assert True == s.isAnagram("anagram","naagram")
assert False  == s.isAnagram("a","")
