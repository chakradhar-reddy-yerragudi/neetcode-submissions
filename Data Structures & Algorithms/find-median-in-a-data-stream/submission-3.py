class MedianFinder:

    def __init__(self):
        self.LeftArr=[]
        self.rightArr=[]
        

    def addNum(self, num: int) -> None:
        if not self.LeftArr:
            heapq.heappush(self.LeftArr,-num)
            return
        
        lLen=len(self.LeftArr)
        rLen=len(self.rightArr)
        if num<=-self.LeftArr[0]:
            heapq.heappush(self.LeftArr,-num)
            if lLen!=rLen:

                heapq.heappush(self.rightArr,-heapq.heappop(self.LeftArr))
              
        else:
            heapq.heappush(self.rightArr,num) 
            if lLen==rLen:
                
                heapq.heappush(self.LeftArr,-heapq.heappop(self.rightArr))


 

    def findMedian(self) -> float:
        lLen=len(self.LeftArr)
        rLen=len(self.rightArr)
        if lLen==rLen:
            return (-self.LeftArr[0]+self.rightArr[0])/2


        else:
            return -self.LeftArr[0]



        

        
        
        