class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp=[]
        ans=[]
    
        
        def backtrack(curr:int)->None:
            if curr==0:
                
                ans.append(''.join(temp))

                return 
            #print(temp)
            openPara=len(temp)-(n-curr)
            closedPara=n-curr
        
            #add open para
            if openPara<n:
                temp.append('(')
                backtrack(curr)
                temp.pop()
            #add closed para
            if closedPara<openPara:
                temp.append(')')
                backtrack(curr-1)
                temp.pop()
    
        backtrack(n)
        return ans
        
            
            

        