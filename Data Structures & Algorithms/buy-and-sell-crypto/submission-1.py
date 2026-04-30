class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  
        maxP = 0 

        while r < len(prices):   
            profit = 0
            if prices[l] < prices[r]:  
                profit = prices[r] - prices[l] 
            else: 
                l = r  
            maxP = max(maxP, profit)
            r += 1
        return maxP

