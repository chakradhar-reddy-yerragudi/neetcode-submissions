
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    q.append((i,j))
                
        
        while q:
            n=len(q)
            for _ in range(n):
                i,j=q.popleft()
                neighbours=[(0,1),(1,0),(0,-1),(-1,0)]
                for h,v in neighbours:

                    if i+h<len(grid) and i+h>=0 and j+v<len(grid[0]) and j+v>=0:
                        if grid[i+h][j+v]==2147483647:
                            q.append((i+h,j+v))
                            grid[i+h][j+v]=grid[i][j]+1

        



       



    

        