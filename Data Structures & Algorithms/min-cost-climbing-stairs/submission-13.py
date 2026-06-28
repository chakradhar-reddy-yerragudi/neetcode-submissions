class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        s=max(sum(cost),1)

        
      
        '''
        for i in range(n-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])

        '''
        dp=[-1 for i in range(n)]
        def backtrack(x)->int:
            if x>=n:
                return 0
            if dp[x]!=-1:
                return dp[x]
            p1=backtrack(x+1)
            p2=backtrack(x+2)
            dp[x]= cost[x]+min(p1,p2)
            return dp[x]
        
        for i in range(2,n):
            cost[i]+=min(cost[i-1],cost[i-2])

    
        return min(cost[n-1],cost[n-2])
    
        

        