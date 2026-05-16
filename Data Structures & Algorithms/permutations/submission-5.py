class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n=len(nums)
        ans=[]
        visited=[0]*n
        curr=[]
        def backtrack(idx:int):

          
            if idx==n:

                ans.append(curr.copy())
                return
           
            for i in range(n):
                if not visited[i]:
                    visited[i]=1
                    curr.append(nums[i])
                    backtrack(idx+1)
                    curr.pop()
                    visited[i]=0

            

        backtrack(0)
        
        return ans