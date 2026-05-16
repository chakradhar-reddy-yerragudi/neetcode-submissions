class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n=len(nums)
        ans=[]
        curr=nums.copy()
        
        def backtrack(idx:int):

          
            if idx==n:
 
                ans.append(curr.copy())
                return
            #print(idx,curr)
           
            for i in range(idx,n):
                curr[idx],curr[i]=curr[i],curr[idx]
                backtrack(idx+1)
                curr[idx],curr[i]=curr[i],curr[idx]
        backtrack(0)

            

      
        
        return ans