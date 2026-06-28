class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1 for i in range(n+2)]
        dp[n]=0
        dp[n+1]=0


        def backtrack(i):

            if dp[i]!=-1:
                return dp[i]


            dp[i]= cost[i]+min(backtrack(i+1),backtrack(i+2))
            return dp[i]
        return min(backtrack(0),backtrack(1))
       