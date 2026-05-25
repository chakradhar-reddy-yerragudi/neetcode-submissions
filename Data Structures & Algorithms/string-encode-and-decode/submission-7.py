class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(str(len(s))+'|'+s)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
       
   
        n=len(s)
        while(i!=n):
            l=i
            while s[i]!='|':
                i+=1
            slen=int(s[l:i])
            res.append(s[i+1:i+slen+1])
            i+=slen+1
        return res


  

