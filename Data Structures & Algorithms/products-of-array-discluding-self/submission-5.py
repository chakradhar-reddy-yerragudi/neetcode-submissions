class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        l=[]
     
        curr=1
        for num in nums:
            l.append(curr)
            curr*=num
        curr=1

        for i in range(n-1,-1,-1):
            l[i]*=curr
            curr*=nums[i]
  
        return l





            
        