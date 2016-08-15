'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
'''
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        i,j = 0,len(nums)-1
        while i<=j:
            if nums[i] == val and nums[j]!=val:
                nums[i] = nums[j];
                nums[j] = val
                i+=1
                j-=1
            elif nums[j] == val:
                j-=1
            else:
                i+=1
        j=len(nums)-1
        while i<=j:
            nums.pop(j)
            j-=1
        return len(nums)

if __name__ == "__main__":
    assert 2 == Solution().removeElement([3,2,2,3],3)