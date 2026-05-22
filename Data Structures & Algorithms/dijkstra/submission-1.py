class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj=defaultdict(list)
        for edge in edges:

            adj[edge[0]].append((edge[1],edge[2]))

        pq=[]
        heapq.heappush(pq,(0,src))
        shortest={}
        #print(adj)
  

        while pq:
            dist,node=heapq.heappop(pq)
            if node in shortest:
                continue
            
            shortest[node]=dist
           
            for nextnode,nextdist in adj[node]:
                heapq.heappush(pq,(dist+nextdist,nextnode))
        for i in range(n):
            if i not in shortest:
                shortest[i]=-1
        return shortest





