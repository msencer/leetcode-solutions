'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
'''
class Solution(object):
    def myAtoi(self, str):
        result, i = 0, 0
        if not str:
            return result
        L = len(str)
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        while i < L and str[i] == " ":
            i += 1

        sign = 1
        if str[i] == "-":
            sign = -1
            i += 1
        elif str[i] == "+":
            i += 1

        while i < L and str[i] >= "0" and str[i] <= "9":
            v = ord(str[i]) - 48
            if result > (INT_MAX - v) / 10:
                return INT_MAX if sign > 0 else INT_MIN
            result = result * 10 + v
            i += 1
        return result * sign

if __name__ == "__main__":
    assert -1234 == Solution().myAtoi("   -1234   ")
    assert 99 == Solution().myAtoi("   +99a    ")