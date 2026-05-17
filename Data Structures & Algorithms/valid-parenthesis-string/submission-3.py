class Solution:

    def checkValidString(self, s: str) -> bool:
        n=len(s)
        dp=[[False]*(n+1) for i in range(n+1)]
        for i in range(n+1):
            dp[n][0]=True
        for i in range(n-1,-1,-1):
            for openCount in range(n):
                if s[i]=='(':
            
                    dp[i][openCount]|= dp[i+1][openCount+1]
              
  
                elif s[i]==')':
                    if not openCount:
                        continue
          
                    dp[i][openCount]|= dp[i+1][openCount-1]
          
                else:
                    if openCount:
                        dp[i][openCount]|= dp[i+1][openCount-1] or dp[i+1][openCount+1] or dp[i+1][openCount]
                    else:
                        dp[i][openCount]|=  dp[i+1][openCount-1] or dp[i+1][openCount]

        return dp[0][0]












        '''
        n=len(s)
        dp={}
        

      

        def backtrack(i:int,openCount:int)->bool:
            if (i,openCount) in dp:
                return dp[(i,openCount)]
            if i==n:
                dp[(i,openCount)]= openCount==0
                return dp[(i,openCount)]
        
            if s[i]=='(':
            
                dp[(i,openCount)]= backtrack(i+1,openCount+1)
                return dp[(i,openCount)]
  
            elif s[i]==')':
                if not openCount:
                    dp[(i,openCount)]=False
                    return dp[(i,openCount)]
          
                dp[(i,openCount)]= backtrack(i+1,openCount-1)
                return dp[(i,openCount)]
            else:
                if openCount:
                    dp[(i,openCount)]= backtrack(i+1,openCount-1) or backtrack(i+1,openCount+1) or backtrack(i+1,openCount)
                else:
                    dp[(i,openCount)]=  backtrack(i+1,openCount+1) or backtrack(i+1,openCount)
                return dp[(i,openCount)]
        return backtrack(0,0)
                
 
        return True
        '''




                

        