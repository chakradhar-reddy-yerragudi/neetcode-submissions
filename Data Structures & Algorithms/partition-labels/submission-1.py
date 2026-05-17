class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        hmap={}
        for i,c in enumerate(s):
            hmap[c]=i
        zeros=0
        unique=set()
        ans=[]
        start=0
        for i,c in enumerate(s):
            unique.add(c)
            if hmap[c]==i:
                zeros+=1
            if len(unique)==zeros:
                ans.append(i-start+1)
                start=i+1
        return ans

        