class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue

            l=i+1
            r=n-1
            while l<r:
                if l!=i+1 and nums[l]==nums[l-1]:
                    l+=1
                    continue
                if nums[l]+nums[r]==-nums[i]:
                    res.append((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif nums[l]+nums[r]>-nums[i]:
                    r-=1
                else:
                    l+=1
        
        return res
        





        