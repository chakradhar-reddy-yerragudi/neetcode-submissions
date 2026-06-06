class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=nums[0]
        l,r=0,len(nums)-1

        while l<=r:
            if nums[l]<=nums[r]:
                ans=nums[l]
                break
            m=l+(r-l)//2
            if nums[l]>nums[m]:
                r=m
            else:
                l=m+1

        
              



        return ans
        
        


        