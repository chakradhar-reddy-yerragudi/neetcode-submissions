class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
        visitsleft=defaultdict(int)
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])
            visitsleft[(ticket[0],ticket[1])]+=1
        
        for edges in adj.values():
            edges.sort()
            
        

        
        curr=[]
        res=[]

        
        n=len(tickets)
        def dfs(location:str,count:int)->bool:
            
            curr.append(location)
            #print(curr,count)
            if count==n:
                
                res.extend(curr)
                curr.pop()
                return True
            
            destinations=adj[location]
            for destination in destinations:
                if visitsleft[(location,destination)]>0:
                    visitsleft[(location,destination)]-=1
                    if dfs(destination,count+1):
                        return True
                    visitsleft[(location,destination)]+=1
            curr.pop()
            return False
            
        dfs('JFK',0)
        return res




        