class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj=defaultdict(set)
        
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        n=len(adj)
        def isConnected():
            q=deque()
            q.append(edges[0][0])

            visited=set()
            visited.add(edges[0][0])
            while q:
                node=q.popleft()
                
                for node2 in adj[node]:
                    if node2 not in visited:
                        q.append(node2)
                        visited.add(node2)
            return len(visited)==n


        
        for i in range(len(edges)-1,-1,-1):
            adj[edges[i][0]].remove(edges[i][1])
            adj[edges[i][1]].remove(edges[i][0])
            if isConnected():
                return [edges[i][0],edges[i][1]]
            adj[edges[i][0]].add(edges[i][1])
            adj[edges[i][1]].add(edges[i][0])
        return []

        

        