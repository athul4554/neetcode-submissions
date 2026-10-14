class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        check = "".join(sorted(s1))
        window = s2[:k]
        if check == "".join(sorted(window)):
            return True
        for i in range(k,len(s2)):
            window=window+s2[i]
            window=window[1:]
            if "".join(sorted(window))==check:
                return True
        return False