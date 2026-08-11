class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht=defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in ht:
                ht[nums[i]]=i
            else:
                return [ht[diff],i]
