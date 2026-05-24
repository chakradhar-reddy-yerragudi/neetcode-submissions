class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1=len(s)
        n2=len(p)
        dp={}
        dp[(n1,n2)]=True


        def backtrack(i,j)->bool:

            if (i,j) in dp:
                return dp[(i,j)]
            if j==n2:
                dp[(i,j)]=False
                return False
         
            match=i<n1 and ((s[i]==p[j])or p[j]=='.')

            if j+1<n2 and p[j+1]=='*':
             
                dp[(i,j)]= (match and backtrack(i+1,j)) or backtrack(i,j+2)
            
            elif match:
                dp[(i,j)]= backtrack(i+1,j+1)

            else:
                dp[(i,j)]= False
            return dp[(i,j)]
        return backtrack(0,0)
            

        