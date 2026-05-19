class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adj=defaultdict(list)
        n=len(grid)
        if n==1:
            return n-1
        for i in range(n):
            for j in range(n):
                if i>0:
                    adj[(i,j)].append((i-1,j))
                if j>0:
                    adj[(i,j)].append((i,j-1))
                if i<n-1:
                    adj[(i,j)].append((i+1,j))
                if j<n-1:
                    adj[(i,j)].append((i,j+1))
        visited=[[0]*n for i in range(n)]
        pq=[]
        heapq.heappush(pq,(grid[0][0],0,0))
        time=0
        while pq:
            maxInPath,i,j=heapq.heappop(pq)
            if visited[i][j]:
                continue
            visited[i][j]=1
            if i==n-1 and j==n-1:
                time=maxInPath
                break

            

            for i1,j1 in adj[(i,j)]:
                if not visited[i1][j1]:
                    heapq.heappush(pq,(max(maxInPath,grid[i1][j1]),i1,j1))
        return time

        

        