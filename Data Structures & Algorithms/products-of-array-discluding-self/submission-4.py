class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zerocount=0
        n=len(nums)
        for num in nums:
            if num ==0:
                zerocount+=1

        if zerocount>1:
            return [0]*len(nums)
        l=[]
     
        curr=1
        for num in nums:
            l.append(curr)
            curr*=num
        curr=1
        res=[]
        for i in range(n-1,-1,-1):
            res.append(l[i]*curr)
            curr*=nums[i]
        res.reverse()
        return res





            
        