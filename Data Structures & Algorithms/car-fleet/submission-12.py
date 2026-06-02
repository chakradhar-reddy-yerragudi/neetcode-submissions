class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if target==0:
            return 1
        

        
        t=[]
        ps=[]
        for i in range(len(speed)):
            ps.append((position[i],speed[i]))
        ps.sort()
        print(ps)
        for i in range(len(speed)):
            if ps[i][1]!=0:

                time=(target-ps[i][0])/ps[i][1]
                while t and t[-1]<=time:
                    t.pop()
                t.append(time)
        print(t)
        return len(t)

        