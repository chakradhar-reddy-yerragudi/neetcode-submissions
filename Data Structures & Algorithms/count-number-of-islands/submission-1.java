class Solution {
    public void dfs(int i,int j,int m,int n,char[][] grid,int [][] visited){
            visited[i][j]=1;
            
            if(i+1<m && visited[i+1][j]!=1 && grid[i+1][j]=='1'){
                dfs(i+1,j,m,n,grid,visited);
            }
            if(j+1<n && visited[i][j+1]!=1 && grid[i][j+1]=='1'){
                dfs(i,j+1,m,n,grid,visited);
            }
            if(i-1>=0 && visited[i-1][j]!=1 && grid[i-1][j]=='1'){
                dfs(i-1,j,m,n,grid,visited);
            }
            if(j-1>=0 && visited[i][j-1]!=1 && grid[i][j-1]=='1'){
                dfs(i,j-1,m,n,grid,visited);
            }
            
        }
    public int numIslands(char[][] grid) {
        int m=grid.length;
        int n=grid[0].length;

        int visited[][]=new int[grid.length][grid[0].length];
        int res=0;

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]=='1' && visited[i][j]==0){
                    this.dfs(i,j,m,n,grid,visited);
                    res+=1;
                }

            }
        }

        

        return res;
        
    }
}
