class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m=max(piles)
        l,r=1,m
        def check(n):
            count=0
            for pile in piles:
                count+=int(math.ceil(pile/n))
            #print(n,count)
            return count<=h
        
        res=m
        while l<=r:
            m=l+(r-l)//2
            if check(m):
                r=m-1
                res=min(m,res)
            else:
                l=m+1
        return res


 



        