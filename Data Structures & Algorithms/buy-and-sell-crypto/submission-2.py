class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf=0
        currBuy=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<currBuy:
                currBuy=prices[i]
            else:
                maxProf=max(prices[i]-currBuy,maxProf)
        return maxProf
        