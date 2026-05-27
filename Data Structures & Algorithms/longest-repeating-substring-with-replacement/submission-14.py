class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        d=defaultdict(int)
        res=0
        replace=0
       
        for i in range(len(s)):
            
                
            d[s[i]]+=1
            
            m=max(d.values())
    
       
            while l<i and i-l+1-m>k:
                d[s[l]]-=1
                m=max(d.values())
                l+=1
           
                    


            
            
            res=max(res,i-l+1)

        return res



        