# Last updated: 11/11/2025, 7:48:00 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        profitMax=0
        while r < len(prices):
            if prices[l] <  prices[r]:
                profit=prices[r]-prices[l]
                profitMax=max(profit,profitMax)
            else:
                l=r
            r+=1
        return profitMax
                

        