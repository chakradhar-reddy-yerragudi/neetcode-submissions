class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)

        def countPalindromes(i:int)->int:

            l=i
            r=i
            count=1

            while l-1>=0 and r+1<n and s[l-1]==s[r+1]:
                l-=1
                r+=1
                count+=1
            

            l2=i
            r2=i+1
           
            while l2>=0 and r2<n and s[l2]==s[r2]:
                count+=1
                l2-=1
                r2+=1
            return count
     
        ans=0
        for i in range(n):
            ans+=countPalindromes(i)

        return ans
        