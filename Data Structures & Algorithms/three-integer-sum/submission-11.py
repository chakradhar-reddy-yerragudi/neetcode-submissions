class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        resSet=set()
        for i in range(n):

            l=i+1
            r=n-1
            while l<r:
                if nums[l]+nums[r]==-nums[i]:
                    resSet.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif nums[l]+nums[r]>-nums[i]:
                    r-=1
                else:
                    l+=1
        
        return list(resSet)
        





        