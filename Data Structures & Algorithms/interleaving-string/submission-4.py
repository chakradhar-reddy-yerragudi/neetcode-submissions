class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        m=len(s1)
        n=len(s2)
        dp=[[False]*(n+1) for i in range(m+1)]

        dp[m][n]=True
      

        for i in range(m,-1,-1):
            for j in range(n,-1,-1):
                if i<m and s1[i]==s3[i+j]:
                    dp[i][j]|=dp[i+1][j]
                if j<n and s2[j]==s3[i+j]:
                    dp[i][j]|=dp[i][j+1]
        return dp[0][0]






        '''
        if len(s1)+len(s2)!=len(s3):
            return False
        m=len(s1)
        n=len(s2)
        dp={}
        dp[(m,n)]=True

        def backtrack(i,j)->bool:
            k=i+j
            if (i,j) in dp:
                return dp[(i,j)]
          

            dp[(i,j)]=False
            if i<m and s1[i]==s3[k]:
                dp[(i,j)]|=backtrack(i+1,j)
            if j<n and s2[j]==s3[k]:
                dp[(i,j)]|=backtrack(i,j+1)
            return dp[(i,j)]
        return backtrack(0,0)
        '''
            




        