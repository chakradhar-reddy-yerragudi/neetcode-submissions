class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1=defaultdict(int)
        d2=defaultdict(int)
        for c in t:
            d1[c]+=1
  
        target=len(d1)
        resl=-1
        resr=-1
        l=0

        count=0
        for i,c in enumerate(s):
            d2[c]+=1
            
            if c in d1 and d1[c]==d2[c]:
                count+=1
            while l<=i and d2[s[l]]>d1[s[l]]:
                d2[s[l]]-=1
                l+=1

            if count==target:
                if resl==-1:
                    resl=l
                    resr=i
                elif i-l<resr-resl:
                    resl=l
                    resr=i



            

        return '' if resl==-1 else s[resl:resr+1]

        