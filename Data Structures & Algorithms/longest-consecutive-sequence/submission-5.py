class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        res=0
        for num in nums:
            if num+1 not in s:
                count=1
                while num-1 in s:
                    count+=1
                    num-=1
                res=max(count,res)
        return res

        


        
       
            
             

        