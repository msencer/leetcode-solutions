'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        L = len(nums)
        if L<=1:
            return L
        removed = 0
        j=0
        for i in xrange(L):
            if nums[i] != nums[j]:
                nums[i],nums[j+1] = nums[j+1],nums[i]
                j+=1
        return j+1

if __name__ == "__main__":
    s = Solution()
    assert 5 == s.removeDuplicates([1,1,2,3,4,4,5])
    assert 4 == s.removeDuplicates([1,2,3,4,4,4,4])
    assert 0 == s.removeDuplicates([])
    assert 1 == s.removeDuplicates([1])