# -*- coding: utf-8 -*-
'''
 Given  an  arbitrary  ransom  note  string  and  another  string  containing  letters from  all  the  magazines,  write  a  function  that  will  return  true  if  the  ransom   note  can  be  constructed  from  the  magazines ;  otherwise,  it  will  return  false.   

Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if not ransomNote:
            return True
        if len(magazine)<len(ransomNote):
            return False
        occurences = [0]*26
        base = ord("a")
        for c in magazine:
            occurences[ord(c)-base]+=1
        for c in ransomNote:
            if occurences[ord(c)-base]<=0:
                return False
            occurences[ord(c)-base]-=1
        return True

if __name__ == "__main__":
    assert True == Solution().canConstruct("","asd")
    assert False == Solution().canConstruct("asd", "")
    assert True == Solution().canConstruct("asdd", "ddasdwqecc")