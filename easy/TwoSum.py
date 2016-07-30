
import sys
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.
'''
class Solution(object):
        def twoSum(self, nums, target):
            s = sorted(nums) # O(nLogn)
            lfor = sys.maxint
            prev = 0
            for i,v in enumerate(nums):
                sfor = target-v
                if lfor<sys.maxint and lfor != v:
                    continue
                if lfor == v:
                    return [prev,i]
                res = self.search(s,sfor)
                if  res>=0:
                   lfor = sfor
                   prev = i
        def search(self,nums,val):
            left,right = 0,len(nums)-1
            while left<=right:
                mid = (left+right)/2
                if nums[mid]<val:
                    left = mid+1
                elif nums[mid]>val:
                    right = mid-1
                else:
                    return mid
            return -1



s = Solution()
assert [0,1] == s.twoSum([2,7,11,15],9)
assert [3,5] == s.twoSum([9,3,4,1,87,2,3],3)
assert [3,4] == s.twoSum([2,1,9,4,4,56,90,3],8)
assert [0,3] == s.twoSum([0,3,4,0],0)
assert [2,4] == s.twoSum([-1,-2,-3,-4,-5],-8)
