class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        for i,num in enumerate(nums):
            l=i-k
            
            while q and q[-1][0]<=num:
                q.pop()
            while q and q[0][1]<=l:
                q.popleft()
            q.append((num,i))
            
            if i>=k-1:

                res.append(q[0][0])
        return res

      
            

        