class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        diagSize=(n*(n+1))//2-1
        
        board=[['.']*n for i in range(n)]
        cols=set()
        diag1=set()
        res=[]

        def backtrack(i:int):
            if i==n:
                res.append([''.join(board[x]) for x in range(n)])
                return
            for j in range(n):
                if j not in cols and i+j not in diag1:
                    diag2=True
                    tempi=i
                    tempj=j
                    while(tempi>=0 and tempj>=0):
                        if board[tempi][tempj]=='Q':
                            diag2=False
                            break
                        tempi-=1
                        tempj-=1
                    if diag2:
                        cols.add(j)
                        diag1.add(i+j)
                        board[i][j]='Q'
                        backtrack(i+1)
                        board[i][j]='.'
                        cols.remove(j)
                        diag1.remove(i+j)
        backtrack(0)
        return res
        