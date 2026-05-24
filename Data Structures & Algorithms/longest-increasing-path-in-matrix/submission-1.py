class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        visited=[[0]*n for i in range(m)]
        dp=[[0]*n for i in range(m)]

        def backtrack(i,j):
            if dp[i][j]:
                return dp[i][j]
            temp=matrix[i][j]
            matrix[i][j]=-1
            dp[i][j]=1

     

            if i+1<m and  matrix[i+1][j]!=-1 and matrix[i+1][j]>temp:
                dp[i][j]=max(dp[i][j],1+backtrack(i+1,j))
            if j+1<n and  matrix[i][j+1]!=-1 and matrix[i][j+1]>temp:
                dp[i][j]=max(dp[i][j],1+backtrack(i,j+1))
            if i-1>=0 and  matrix[i-1][j]!=-1 and matrix[i-1][j]>temp:
                dp[i][j]=max(dp[i][j],1+backtrack(i-1,j))
            if j-1>=0 and  matrix[i][j-1]!=-1 and matrix[i][j-1]>temp:
                dp[i][j]=max(dp[i][j],1+backtrack(i,j-1))
            matrix[i][j]=temp
            return dp[i][j]
            
        res=1
        for i in range(m):
            for j in range(n):
                res=max(res,backtrack(i,j))
        return res






        