class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr=[]
        res=[]
        visited=set()
        def backtrack(i):
            #print(i,curr)
            
            if len(curr)==k:
                res.append(curr.copy())
                return
            if i==n+1:
                return

            backtrack(i+1)
            curr.append(i)
            backtrack(i+1)
            curr.pop()
        backtrack(1)
        return res
        