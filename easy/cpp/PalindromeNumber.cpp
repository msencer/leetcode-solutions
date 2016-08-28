
/*
Determine whether an integer is a palindrome. Do this without extra space.

*/

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        
        int initial = x;
        int reverse = 0;
        
        while (x > 0)
        {
            int dig = x % 10;
            reverse = reverse * 10 + dig;
            x = x / 10;
        }
        return (initial == reverse);
    }
};