class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        m=len(s1)
        n=len(s2)
        dp={}
        dp[(m,n,1)]=True
        dp[(m,n,2)]=True

        def backtrack(i,j,stringNumber):
            k=i+j
           # if k==m+n:
            #    return True
            if (i,j,stringNumber) in dp:
                return dp[(i,j,stringNumber)]

            dp[(i,j,stringNumber)]=False
            print(k)

            
            if stringNumber==1:
                tempi=i
                while tempi<m:
                    if s1[tempi]==s3[k]:
                 
                        dp[(i,j,stringNumber)]|=backtrack(tempi+1,j,2)
                        tempi+=1
                        k+=1
                    else:
                        break
            else:
                tempj=j
                while tempj<n:
                    if s2[tempj]==s3[k]:
                        dp[(i,j,stringNumber)]|=backtrack(i,tempj+1,1)
                        tempj+=1
                        k+=1
                    else:
                        break
            return dp[(i,j,stringNumber)]
        return backtrack(0,0,1) or backtrack(0,0,2)
            




        