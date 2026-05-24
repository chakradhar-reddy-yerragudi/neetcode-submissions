class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        visited=[[0]*n for i in range(m)]
        dp=[[0]*n for i in range(m)]

        def backtrack(i,j):
            if dp[i][j]:
                return dp[i][j]
            visited[i][j]=1
            dp[i][j]=1

     

            if i+1<m and not visited[i+1][j] and matrix[i+1][j]>matrix[i][j]:
                dp[i][j]=max(dp[i][j],1+backtrack(i+1,j))
            if j+1<n and not visited[i][j+1] and matrix[i][j+1]>matrix[i][j]:
                dp[i][j]=max(dp[i][j],1+backtrack(i,j+1))
            if i-1>=0 and not visited[i-1][j] and matrix[i-1][j]>matrix[i][j]:
                dp[i][j]=max(dp[i][j],1+backtrack(i-1,j))
            if j-1>=0 and not visited[i][j-1] and matrix[i][j-1]>matrix[i][j]:
                dp[i][j]=max(dp[i][j],1+backtrack(i,j-1))
            visited[i][j]=0
            return dp[i][j]
            
        res=1
        for i in range(m):
            for j in range(n):
                res=max(res,backtrack(i,j))
        return res






        