class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hs = set(nums)
        max_count=0
        count=0
        for i in hs:
            if i-1 not in hs:
                current=i
                count=1
                while (current + 1) in hs:
                    current+=1
                    count+=1
            max_count=max(count,max_count)
        return max_count


        