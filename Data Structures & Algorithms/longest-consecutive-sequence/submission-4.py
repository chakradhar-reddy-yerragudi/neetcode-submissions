class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap={}
        res=0
        for num in nums:
            if num not in hmap:
                hmap[num]=num
            if num-1 in hmap:
                hmap[num-1]=num
            if num+1 in hmap:
                hmap[num]=num+1
        for num in hmap:
            if hmap[num]==num:
                count=1
                while num-1 in hmap:
                    num-=1
                    count+=1
                res=max(count,res)
        return res


        
       
            
             

        