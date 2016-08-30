# coding=utf-8
"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""


class NumArray(object):
    def __init__(self, nums):
        numsLength = len(nums)
        self.cumulative = [0] * numsLength
        if not numsLength:
            return
        self.cumulative[0] = nums[0]
        for i in xrange(1, numsLength):
            self.cumulative[i] = self.cumulative[i - 1] + nums[i]

    def sumRange(self, i, j):
        if i > j or i > len(self.cumulative) - 1 or j > len(self.cumulative) - 1:
            return 0
        if i == 0:
            return self.cumulative[j]
        if i == j:
            return self.cumulative[j] - self.cumulative[j - 1]

        return self.cumulative[j] - self.cumulative[i - 1]

if __name__ == "__main__":
    nums = NumArray([-2, 0, 3, -5, 2, -1])
    assert 1 == nums.sumRange(0,2)
    assert -1 == nums.sumRange(2,5)
    assert -3 == nums.sumRange(0,5)
