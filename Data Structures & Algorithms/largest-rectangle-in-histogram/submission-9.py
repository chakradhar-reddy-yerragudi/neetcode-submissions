class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        lsmaller=[]
        

        stk=[]
        for i in range(len(heights)):
            while stk and heights[stk[-1]]>=heights[i]:
                stk.pop()
            if stk:
                lsmaller.append(stk[-1])
            else:
                lsmaller.append(-1)
            stk.append(i)
        #print(lsmaller)
        res=0
        stk=[]
        for i in range(len(heights)-1,-1,-1):
            while stk and heights[stk[-1]]>=heights[i]:
                stk.pop()
            
            if stk:
                #print(heights[i],stk[-1],i,lsmaller[i])

                res=max((stk[-1]-lsmaller[i]-1)*heights[i],res)
            else:
                res=max((len(heights)-lsmaller[i]-1)*heights[i],res)
            stk.append(i)
        return res




            
            
        

      
       
        return 
        
        
        
        

            

        