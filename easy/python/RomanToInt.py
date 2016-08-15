'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    def romanToInt(self, s):
        lookup = {'I':1,'V':5,'X':10,"L":50,"C":100,"D":500,"M":1000}
        s = s.upper()
        q = []
        result = 0
        for c in s:
            prev = 0
            if q:
                prev = q[-1]
            if prev and lookup.get(c)>prev:
                result += (lookup.get(c)-prev)
                q.pop()
            else:
                q.append(lookup.get(c))
        while q:
            el = q.pop()
            result+=el
        return result

if __name__ == "__main__":
    assert 222 == Solution().romanToInt("CCXXII")
    assert 1553 == Solution().romanToInt("MDLIII")

