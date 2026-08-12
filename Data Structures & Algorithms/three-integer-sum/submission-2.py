class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr=[]
        nums=sorted(nums)
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while(l<r):
                if nums[i]+nums[l]+nums[r]==0:
                    if sorted([nums[i],nums[l],nums[r]]) not in arr:
                        arr.append(sorted([nums[i],nums[l],nums[r]]))
                    l+=1
                    r-=1
                    continue
                if nums[i]+nums[l]+nums[r]>0:
                    r-=1
                    continue
                if nums[i]+nums[l]+nums[r]<0:
                    l+=1
                    continue
        return arr