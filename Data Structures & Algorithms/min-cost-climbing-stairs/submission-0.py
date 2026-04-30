class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # im gonna simulate a decision tree with dp 
        # ill iterate in reverse order because i have to update cost[i] depending on  
        # the minumum cost for it between it jumping 1 step to the right or 2 
        # in the end ill only need to return th eminum cost between step 1 and 0 and i know those will contain 
        # the minumum costs from their "subtrees" i simulated by going in reverse order 
        # also im gonna add an imaginary 0 for the math to work because the last position can only go 1 step to the right 
        # so it wouldnt even have a cost + 2 it can only go cost + 1 

        cost.append(0)  
        # [1 , 2 , 3 , 0] 
        # []

        for i in range(len(cost) - 3, - 1, - 1): 
            cost[i] += min(cost[i + 1], cost[i + 2])  
            
        return min(cost[0], cost[1]) 
