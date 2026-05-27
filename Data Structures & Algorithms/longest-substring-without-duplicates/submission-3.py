class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset=set()
        l=0
        res=0
        for i in range(len(s)):

            
            while s[i] in hset:
                hset.remove(s[l])
                l+=1
            if l<=i:
                hset.add(s[i])

            res=max(i-l+1,res)
            

        


        return res


        