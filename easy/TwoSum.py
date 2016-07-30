
import sys
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.
'''
class Solution(object):
        def twoSum(self, nums, target):
            lookup = {}
            for i,v in enumerate(nums):
                if target-v in lookup:
                    return [lookup[target-v],i]
                lookup[v]=i


s = Solution()
assert [0,1] == s.twoSum([2,7,11,15],9)
assert [3,5] == s.twoSum([9,3,4,1,87,2,3],3)
assert [3,4] == s.twoSum([2,1,9,4,4,56,90,3],8)
assert [0,3] == s.twoSum([0,3,4,0],0)
assert [2,4] == s.twoSum([-1,-2,-3,-4,-5],-8)
assert [1,2] == s.twoSum([3,2,4],6)
