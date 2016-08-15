'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
'''
class Solution(object):
    def isNumber(self, s):

        INVALID = 0;
        SIGN = 1;
        DIGIT = 2;
        EXP = 3;
        DOT = 4;
        SPACE = 5;
        transitions = [
            [-1, 1, 2, -1, 3, 0],
            [-1, -1, 2, -1, 3, -1],
            [-1, -1, 2, 5, 4, 8],
            [-1, -1, 4, -1, -1, -1],
            [-1, -1, 4, 5, -1, 8],
            [-1, 6, 7, -1, -1, -1],
            [-1, -1, 7, -1, -1, -1],
            [-1, -1, 7, -1, -1, 8],
            [-1, -1, -1, -1, -1, 8]];

        state = 0;
        i = 0
        while i < len(s):
            inputtype = INVALID
            if s[i] == ' ':
                inputtype = SPACE
            elif s[i] == '-' or s[i] == '+':
                inputtype = SIGN
            elif "0" <= s[i] <= "9":
                inputtype = DIGIT
            elif s[i] == '.':
                inputtype = DOT
            elif s[i] == 'e' or s[i] == 'E':
                inputtype = EXP

            state = transitions[state][inputtype]
            if state == -1:
                return False
            else:
                i += 1
        return state == 2 or state == 4 or state == 7 or state == 8

if __name__ == "__main__":
    assert False == Solution().isNumber("9e")
    assert True == Solution().isNumber(".9")
    assert True == Solution().isNumber("004543e+9")