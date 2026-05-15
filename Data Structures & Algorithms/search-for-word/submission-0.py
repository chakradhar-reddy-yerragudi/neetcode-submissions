class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        visited=[[0]*n for i in range(m)]
        wLen=len(word)

        def backtrack(i,j,w):
            #print(w,i,j)


            if word[w]!=board[i][j]:
                return False
            
            visited[i][j]=1
            if w==wLen-1:
                return True

            if i+1<m and  not visited[i+1][j]:
                if backtrack(i+1,j,w+1):
                    visited[i][j]=0
                    return True
            if i-1>=0 and  not visited[i-1][j]:
                if backtrack(i-1,j,w+1):
                    visited[i][j]=0
                    return True
            if j+1<n and  not visited[i][j+1]:
                if backtrack(i,j+1,w+1):
                    visited[i][j]=0
                    return True
            if j-1>=0 and  not visited[i][j-1]:
                if backtrack(i,j-1,w+1):
                    visited[i][j]=0
                    return True
            visited[i][j]=0
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0):
                    return True
        return False
            
        