'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''
class Solution(object):
    def plusOne(self, digits):
        if not digits:
            return [1]

        c = 1
        i = len(digits) - 1
        while i >= 0:
            v = digits[i]
            digits[i] = (v + c) % 10
            c = (v + c) // 10
            i -= 1
        if c:
            digits = [1] + digits
        return digits

if __name__ == "__main__":
    assert [1,0,0,0] == Solution().plusOne([9,9,9])
    assert [7, 6, 8, 9] == Solution().plusOne([7, 6, 8, 8])
    assert [1,0] == Solution().plusOne([9])