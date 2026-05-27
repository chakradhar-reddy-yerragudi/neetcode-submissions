class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1=defaultdict(int)

        for c in s1:
     
            d1[c]+=1


        d2=defaultdict(int)
        l=0
        count=0

        for i,c in enumerate(s2):
      
            d2[c]+=1
            count+=1

            while d2[c]>d1[c]:
                count-=1
                d2[s2[l]]-=1
                l+=1

     
            if count==len(s1):
                return True
        return False


            

     
        
        

        