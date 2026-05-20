class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n=len(words)
        adj={}
        for i in range(n):
            for c in words[i]:
                if c not in adj:
                    adj[c]=set()
            
            if i!=n-1:
                m=len(words[i+1])
                differences=0
                for j,c in enumerate(words[i]):
                    if j<m:   
                        if c!=words[i+1][j]:
                            differences+=1
                            adj[c].add(words[i+1][j])
                            break
                if not differences and len(words[i])>len(words[i+1]):
                    return ''
        res=[]
 
        visited=set()
        path=set()

        def dfs(c:str)->bool:
            if c in path:
                return False
            if c in visited:
                return True
            
            visited.add(c)
            path.add(c)

            for child in adj[c]:
                if not dfs(child):
                    return False
            res.append(c)
            path.remove(c)
            return True
            
        for c in adj:
            if not dfs(c):
                return ''



        res.reverse()

        return ''.join(res)


        '''
        e<r
        w<r
        r<t
        t<f
        f<e

        '''





            
        