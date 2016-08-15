'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution(object):
    def rob(self, nums):
        L = len(nums)
        if L == 0:
            return 0
        if L == 1:
            return nums[0]
        num_0,num_1 = max(nums[0],nums[1]),nums[0]
        for i in range(2,L):
            num_1,num_2 = num_0,num_1
            num_0 = max(nums[i]+num_2,num_1)
        return num_0

if __name__ == "__main__":
    assert 19 == Solution().rob([8,1,2,3,3,5,6])
    assert 11 == Solution().rob([1,2,1,3,9,1])