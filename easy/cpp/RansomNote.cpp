/*
Given  an  arbitrary  ransom  note  string  and  another  string  containing  letters from  all  the  magazines,  write  a  function  that  will  return  true  if  the  ransom   note  can  be  constructed  from  the  magazines ;  otherwise,  it  will  return  false.   

Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.
Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
*/
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.size() == 0) return true;
        if (magazine.size() == 0)   return false;
        
        map<char, int> availableChars;
        
        for (int i = 0; i < magazine.size(); i++)
        {
            availableChars[magazine[i]]++;
        }
        for (int i = 0; i < ransomNote.size(); i++)
        {
            if (availableChars.find(ransomNote[i]) == availableChars.end())
                return false;
            availableChars[ransomNote[i]]--;
            if (availableChars[ransomNote[i]] < 1)
                availableChars.erase(ransomNote[i]);
        }
        
        return true;
    }
};