class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[1],flight[2]))
        
        pq=[]
        heapq.heappush(pq,(0,src,0))
        dstcost=-1
        
        
        while pq:
            cost,flight,stopnumber=heapq.heappop(pq)
            if flight==dst:
                if stopnumber<=k+1:
                    dstcost=cost
                    break
            

            for destination in adj[flight]:
                heapq.heappush(pq,(cost+destination[1],destination[0],stopnumber+1))




        return dstcost

        