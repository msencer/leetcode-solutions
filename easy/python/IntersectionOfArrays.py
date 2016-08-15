'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
    Each element in the result must be unique.
    The result can be in any order.
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        nums = {}
        res = []
        for i in nums2:
            nums[i] = 0
        for i in nums1:
            if i in nums:
                nums[i]+=1
        for k in nums.keys():
            if nums[k] >0:
                res.append(k)
        return res

if __name__ == "__main__":
    assert [2] == Solution().intersection([1,2,2,1],[2,2])
    assert [] == Solution().intersection([1,2,2,1],[])
    assert [1,2,3] == Solution().intersection([1,2,3,4,5,5,5],[1,1,2,3,3])