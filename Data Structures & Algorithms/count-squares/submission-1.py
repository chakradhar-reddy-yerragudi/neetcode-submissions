class CountSquares:

    def __init__(self):
        self.points=[]
        

    def add(self, point: List[int]) -> None:
        self.points.append(tuple(point))
        

    def count(self, point: List[int]) -> int:
        def isSquare(s:set):
            if len(s)<4:
                return False
            lowerLeft=min(s)
            upperRight=max(s)
            s.remove(lowerLeft)
            s.remove(upperRight)
            
         
            if (upperRight[0],lowerLeft[1]) not in s:
                return False
            if (lowerLeft[0],upperRight[1]) not in s:
                return False
             
            #print(arr)
            print(lowerLeft,upperRight)


            return True
        n=len(self.points)
        count=0
        print(self.points)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    s=set()
                    s.add((point[0],point[1]))
                    s.add(self.points[i])
                    s.add(self.points[j])
                    s.add(self.points[k])
                    
                    if isSquare(s):
                        print(i,j,k)
                        count+=1
        return count
        
