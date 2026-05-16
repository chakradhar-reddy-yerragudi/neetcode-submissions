class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n=len(nums)
        ans=[]
        visited=[0]*n
        curr=[]
        nums.sort()
        def backtrack(idx:int):

          
            if idx==n:
           
                ans.append(curr.copy())
                return
           
            for i in range(n):
                if not visited[i]:
                    if i!=0 and  nums[i]==nums[i-1] and not visited[i-1]:
                        continue
                    visited[i]=1
                    curr.append(nums[i])
                    backtrack(idx+1)
                    curr.pop()
                    visited[i]=0

            

        backtrack(0)
        
        return ans