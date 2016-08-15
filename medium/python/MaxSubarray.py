# coding=utf-8
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''
class Solution(object):
    def maxSubArray(self, nums):
        l = len(nums)
        if not l:
            return 0
        if l == 1:
            return nums[0]

        result, currentSum = nums[0], nums[0]
        i = 1
        while i < l:
            currentSum = max(currentSum + nums[i], nums[i])
            result = max(result, currentSum)
            i += 1
        return result

if __name__ == "__main__":
    assert 28 == Solution().maxSubArray([-2,3,4,15,-3,2,3,4])