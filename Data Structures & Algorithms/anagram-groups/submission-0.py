class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht={}
        for i in strs:
            if tuple(sorted(i)) in ht:
                ht[tuple(sorted(i))].append(i)
            else:
                ht[tuple(sorted(i))]=[i]
        return list(ht.values())
        