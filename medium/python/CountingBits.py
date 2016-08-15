# coding=utf-8
'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2]

'''
class Solution(object):
    def countBits(self, num):
        result = [0] * (num+1)
        i = 1
        while i<=num:
            if i%2:
                result[i] = result[i-1] + 1
            else:
                result[i] = result[i/2]
            i+=1
        return result

if __name__ == "__main__":
    assert [0,1,1,2,1,2] == Solution().countBits(5)