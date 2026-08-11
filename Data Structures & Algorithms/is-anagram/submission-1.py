class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Str1,Str2 = {},{}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            Str1[s[i]] = 1 + Str1.get(s[i],0)
            Str2[t[i]] = 1 + Str2.get(t[i],0)
        if(Str2 == Str1):
            return True
        return False
        