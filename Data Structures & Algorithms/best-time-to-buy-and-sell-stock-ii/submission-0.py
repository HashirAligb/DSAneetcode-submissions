class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l will be my holding pos  

        maxP = 0 
        l = 0 

        for r in range(len(prices)): 
            if prices[r] > prices[l]: 
                maxP += (prices[r] - prices[l]) 
                l = r 
            elif prices[r] < prices[l]: 
                l = r  
        return maxP
