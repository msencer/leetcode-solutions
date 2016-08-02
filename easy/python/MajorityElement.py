class Solution(object):
        def majorityElement(self, nums):
            l = len(nums)
            if l<3:
                return nums[0]
            return sorted(nums)[int(l/2)]


s = Solution()
assert 5 == s.majorityElement([1,2,5,3,5,6,5,5,1,5,5])
assert 1 == s.majorityElement([1])
assert 2 == s.majorityElement([2,1,2])
