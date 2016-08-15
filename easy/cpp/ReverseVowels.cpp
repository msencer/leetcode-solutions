/*
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
*/
class Solution {
public:
    bool isVowel(char inp){
        switch(inp){
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
                return true;
            default:
                return false;
        }
    }
    string reverseVowels(string s) {
        int f = 0;
        int t = s.length();

        //unordered_set<char> vowels ( {'a','e','i','o','u','A','E','I','O','U'} );
        while(f<=t-1){
            if(isVowel(s[f]) && isVowel(s[t]))
            {
                char temp = s[f];
                s[f] = s[t];
                s[t] = temp;
                f++;
                t--;
            }
            if(!isVowel(s[f])){
                f++;
            }
            if(!isVowel(s[t])){
                t--;
            }
        }

        return s;
    }
};