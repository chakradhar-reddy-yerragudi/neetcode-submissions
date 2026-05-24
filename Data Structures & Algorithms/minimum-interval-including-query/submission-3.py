class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort(key=lambda x: (x[0],x[1]))
 
        qcopy=[(queries[i],i) for i in range(len(queries))]
        qcopy.sort(key=lambda x:x[0])
        pq=[]
        n=len(intervals)
        i=0
        res=[-1 for i in range(len(queries))]
        #print(intervals)
        for query,index  in qcopy:
            while i<n and query>=intervals[i][0]:

                heapq.heappush(pq,(intervals[i][1]-intervals[i][0]+1,intervals[i][1]))
                i+=1
            #print(query,index,pq,i)
            while pq and (query>pq[0][1]):
                heapq.heappop(pq)
            
            if pq:
                res[index]=pq[0][0]

        return res


        #[1,3],[2,3],[3,7],[6,6]], queries = [1,2,3,6,7,8]

        