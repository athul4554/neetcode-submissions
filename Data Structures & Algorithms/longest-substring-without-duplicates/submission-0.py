class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs=set()
        count = 0
        start=0
        for i in s:
            while i in hs:
                hs.remove(s[start])
                start+=1
            hs.add(i)
            count = max(count,len(hs))
        return count

        