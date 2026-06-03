class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)
        while l<r:
            m=l+(r-l)//2

            if target<=nums[m]:
                r=m
            else:
                l=m+1
        print(l)
        return r if r<len(nums) and nums[r]==target else -1