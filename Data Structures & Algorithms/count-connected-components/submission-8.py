class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        hmap={}
        for i in range(n):
            hmap[i]=i

        for edge in edges:
            curr1=edge[0]
            curr2=edge[1]
            count1=0
            count2=0
            
            while hmap[curr1]!=curr1:
                curr1=hmap[curr1]
                count1+=1
            while hmap[curr2]!=curr2:
                curr2=hmap[curr2]
                count1+=1
            if count1>count2:
                hmap[curr2]=curr1
            else:
                hmap[curr1]=hmap[curr2]
            
        count=0
        for i in range(n):
            if hmap[i]==i:
                count+=1
        return count


      

        


        


        
        

            
        