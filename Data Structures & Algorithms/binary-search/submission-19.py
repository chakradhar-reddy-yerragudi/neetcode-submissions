class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)
        while l<r:
            m=l+(r-l)//2

            if target>=nums[m]:
                l=m+1
            else:
                r=m
        print(l)
        return l-1 if l>0 and nums[l-1]==target else -1