class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(str(len(s))+'|'+s)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        res=[]
        l=0
        r=0
        temp=list(s)
        n=len(s)
        while(l!=n):
            while temp[r]!='|':
                r+=1
            slen=0

            for i in range(l,r):
                slen=10*slen+int(temp[i])
            res.append(temp[r+1:r+slen+1])
            l=r+slen+1
            r=r+slen+1
        return [''.join(arr) for arr in res]


  

