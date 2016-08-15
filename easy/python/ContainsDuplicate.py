'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for i in nums:
            s.add(i)
        return len(s) != len(nums)

if __name__ == "__main__":
    assert True == Solution().containsDuplicate([1,2,3,3,4])
    assert False == Solution().containsDuplicate([])
    assert False == Solution().containsDuplicate([1,2,3,4])
