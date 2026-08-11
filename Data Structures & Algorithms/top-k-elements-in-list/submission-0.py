class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht=defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in ht:
                ht[nums[i]]+=1
            else:
                ht[nums[i]]=1

        sort_ht = sorted(ht,key=ht.get,reverse=True)
        return sort_ht[:k]
