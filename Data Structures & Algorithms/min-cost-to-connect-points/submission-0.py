class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq=[]
        visited=set()
        cost=0
        adj=defaultdict(list)
        n=len(points)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    xi=points[i][0]
                    yi=points[i][1]
                    xj=points[j][0]
                    yj=points[j][1]
                    adj[(xi,yi)].append((abs(xi-xj)+abs(yi-yj),xj,yj))
        
        heapq.heappush(pq,(0,points[0][0],points[0][1]))

        while pq:
            costi,xi,yi=heapq.heappop(pq)
            if (xi,yi) in visited:
                continue
            cost+=costi
            visited.add((xi,yi))
            #print(xi,yi)
            if len(visited)==n:
                break
            for costj,xj,yj in adj[(xi,yi)]:
                if (xj,yj) not in visited:
                    #print(costj,xj,yj)
                    heapq.heappush(pq,(costj,xj,yj))
        
        return cost
            

        