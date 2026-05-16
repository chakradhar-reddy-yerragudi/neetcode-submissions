class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        curr=[]

        nums.sort()
        ans=[]
     

        def backtrack(i:int):
            if i==n:
                print(curr)
                ans.append(curr.copy())
                return
           
            
            
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
        
            if i+1<n and nums[i]==nums[i+1]:
                j=i+1
                while j+1<n and nums[j]==nums[j+1]:
                    j+=1
                backtrack(j+1)
            else:
                backtrack(i+1)
        
        backtrack(0)
  
        return ans
        

        