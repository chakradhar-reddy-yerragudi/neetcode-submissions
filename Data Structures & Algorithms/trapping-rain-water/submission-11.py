class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lmax=0
        rmax=0
        res=0
        while l<=r:
            lmax=max(lmax,height[l])
            rmax=max(rmax,height[r])
            if height[l]>height[r]:
                res+=max(0,min(lmax,rmax)-height[r])
                r-=1
            else:
                res+=max(0,min(lmax,rmax)-height[l])
                l+=1

            
        return res




            
        