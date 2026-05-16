class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(nums)
        temp=[]
        #s=set()
       

        def getCombinations(target:int,i:int,curr:int)->None:
            if curr==target:
                ans.append(temp.copy())
                return
            if i==n or curr>target:
                return
            
            getCombinations(target,i+1,curr)
            temp.append(nums[i])
            getCombinations(target,i,curr+nums[i])
            temp.pop()
          
            
        getCombinations(target,0,0)
        return ans

        