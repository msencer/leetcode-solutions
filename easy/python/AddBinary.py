"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution(object):
    def addBinary(self, a, b):
        i, j = len(a) - 1, len(b) - 1
        result = []
        carry = 0
        base = ord("0")
        while i >= 0 and j >= 0:
            first = ord(a[i]) - base
            second = ord(b[j]) - base

            result.append(str(first ^ second ^ carry))
            carry = (first & second) | carry & (first ^ second)
            i -= 1
            j -= 1
        while i >= 0:
            first = ord(a[i]) - base
            result.append(str(first ^ carry))
            carry &= first
            i -= 1
        while j >= 0:
            first = ord(b[j]) - base
            result.append(str(first ^ carry))
            carry &= first
            j -= 1
        if carry:
            result.append("1")

        return "".join(result[::-1])


if __name__ == "__main__":

    assert "1100" == Solution().addBinary("1011", "1")
    assert "10" == Solution().addBinary("1", "1")
    assert "10010101" == Solution().addBinary("10010000", "101")
