class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        m=len(triplets)
        n=len(triplets[0])
        targetCheck=[False for i in range(n)]
        for i in range(m):
            usefulTriplet=True
            for j in range(n):
                if triplets[i][j]>target[j]:
                    usefulTriplet=False
                    break
            if usefulTriplet:
                for j in range(n):
                    if triplets[i][j]==target[j]:
                        targetCheck[j]=True
        
        for i in range(n):
            if not targetCheck[i]:
                return False
        return True

        