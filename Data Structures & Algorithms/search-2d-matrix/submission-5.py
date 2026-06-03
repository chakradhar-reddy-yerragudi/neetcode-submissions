class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l,r=0,len(matrix)

        while l<r:
            m=l+(r-l)//2
            if target<=matrix[m][0]:
                r=m
            else:
                l=m+1

        if l==len(matrix) or matrix[l][0]>target:
            l-=1
    
        if l<0:
            return False
        l1,r1=0,len(matrix[0])-1
        while l1<=r1:
            m=l1+(r1-l1)//2
            if matrix[l][m]==target:
                return True
            elif target<matrix[l][m]:
                r1=m-1
            else:
                l1=m+1
        return False


            


        
            
        