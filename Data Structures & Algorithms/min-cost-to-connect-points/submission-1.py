class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent={(xi,yi):(xi,yi) for xi,yi in points}
        rank={(xi,yi):0 for xi,yi in points}

        def find(xi,yi):

            while parent[(xi,yi)]!=(xi,yi):
                parent[(xi,yi)]=parent[parent[(xi,yi)]]
                xi,yi=parent[(xi,yi)]
            return xi,yi
        def union(xi,yi,xj,yj):
            xi,yi=find(xi,yi)
            xj,yj=find(xj,yj)
            if (xi,yi)==(xj,yj):
                return False

            if rank[(xi,yi)]>rank[(xj,yj)]:
                parent[(xj,yj)]=(xi,yi)
            elif rank[(xi,yi)]<rank[(xj,yj)]:
                parent[(xi,yi)]=(xj,yj)
            else:
                parent[(xi,yi)]=(xj,yj)
                rank[(xj,yj)]+=1
            return True
        
        pq=[]
        for xi,yi in points:
            for xj,yj in points:
                if (xi,yi)!=(xj,yj):
                    heapq.heappush(pq,(abs(xi-xj)+abs(yi-yj),xi,yi,xj,yj))
        res=0
        count=0
        n=len(points)
        while pq:
            cost,xi,yi,xj,yj=heapq.heappop(pq)

            if union(xi,yi,xj,yj):
                res+=cost
                count+=1
            if count==n-1:
                break
        return res






        '''
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
        '''
            

        