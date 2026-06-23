

class Solution {
    public int dfs(int i,int j,int m,int n,int [][]visited,int [][] grid){
        visited[i][j]=1;
        int count=1;
        if(i+1<m && grid[i+1][j]==1&&visited[i+1][j]==0){
            count+=this.dfs(i+1,j,m,n,visited,grid);
        }
        if(j+1<n && grid[i][j+1]==1&&visited[i][j+1]==0){
            count+=this.dfs(i,j+1,m,n,visited,grid);
        }

        if(i-1>=0 && grid[i-1][j]==1&&visited[i-1][j]==0){
            count+=this.dfs(i-1,j,m,n,visited,grid);
        }
        if(j-1>=0 && grid[i][j-1]==1&&visited[i][j-1]==0){
            count+=this.dfs(i,j-1,m,n,visited,grid);
        }

        return count;


    }
    public int maxAreaOfIsland(int[][] grid) {
        int m=grid.length;
        int n=grid[0].length;
        int visited[][]=new int[grid.length][grid[0].length];
        int res=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==1&&visited[i][j]==0){
                    res=Math.max(this.dfs(i,j,m,n,visited,grid),res);
                }
            }
        }
        return res;

        

        
    }
}
