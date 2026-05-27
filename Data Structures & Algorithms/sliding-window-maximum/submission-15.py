class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq=[]
        res=[]
        for i,num in enumerate(nums):
            heapq.heappush(pq,(-num,i))
            if i>=k-1:
                l=i-k
                while pq[0][1]<=l:
                    heapq.heappop(pq)
                res.append(-pq[0][0])
        return res

      
            

        