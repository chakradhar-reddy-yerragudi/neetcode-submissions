class Solution:
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        
        
      
        parent={}
        rank={}
        for edge in edges:
            parent[edge[0]]=edge[0]
            parent[edge[1]]=edge[1]
            rank[edge[0]]=1
            rank[edge[1]]=1
    

        def find(a):

            while parent[a]!=a:
                parent[a]=parent[parent[a]]
                a=parent[a]
            return a
        def union(a,b):
            a=find(a)
            b=find(b)
            if a==b:
                return False
            if rank[a]>rank[b]:
                parent[b]=a
            elif rank[b]>rank[a]:
                parent[a]=b
            else:
                parent[a]=b
                rank[b]+=1


            return True
        for edge in edges:
            if not union(edge[0],edge[1]):
                return [edge[0],edge[1]]
        return []




  
        

        