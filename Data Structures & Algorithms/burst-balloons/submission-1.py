class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        curr=[]
   
        nums.append(1)
        nums.insert(0,1)
        n=len(nums)
        dp=[[-1]*(n+1) for i in range(n+1)]



        def backtrack(l:int,r:int)->int:
            if dp[l][r]!=-1:
                return dp[l][r]
            if l==r:
                dp[l][r]= nums[l-1]*nums[l]*nums[l+1]
                return dp[l][r]
            dp[l][r]=0
            for i in range(l,r+1):
                if i==l:
                    dp[l][r]=max(nums[l-1]*nums[i]*nums[r+1]+backtrack(i+1,r),dp[l][r])
                elif i==r:
                    dp[l][r]=max(nums[l-1]*nums[i]*nums[r+1]+backtrack(l,i-1),dp[l][r])
                else:
                    dp[l][r]=max(nums[l-1]*nums[i]*nums[r+1]+backtrack(l,i-1)+backtrack(i+1,r),dp[l][r])
            return dp[l][r]
        return backtrack(1,n-2)
        


            


        