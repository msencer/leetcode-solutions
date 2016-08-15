'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
'''

import random
class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        output = self.nums[:]
        n = len(output)
        for i in xrange(n):
            _id = random.randint(i, n - 1)
            output[i], output[_id] = output[_id], output[i]
        return output
if __name__ == "__main__":
     obj = Solution([1,2,3])
     param_1 = obj.reset()
     print obj.shuffle()