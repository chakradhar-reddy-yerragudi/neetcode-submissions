class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency=[[] for i in range(len(nums)+1)]
        counts=defaultdict(int)
        for num in nums:
            counts[num]+=1

        for num,count in counts.items():
            frequency[count].append(num)
        res=[]
        for i in range(len(nums),-1,-1):
            while frequency[i] and k:
                res.append(frequency[i][-1])
                frequency[i].pop()
                k-=1
            if k==0:
                break
        return res


        