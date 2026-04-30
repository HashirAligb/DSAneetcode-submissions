class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # the approach i will make here is go through all my indices and keep track of total 
        # total is my cost - the gas i have 
        # before i do that though, i will verify if the sum of my gas and cost is the same 
        # if it is the same that means im guranteed atleast one solution, and that there will be a loop 
        # i will keep track of my starting position by simply updating my res to i + 1 everytime 
        # total sinks beneath 0  
        if sum(gas) < sum(cost): 
            return -1

        res = 0  
        total = 0

        for i in range(len(gas)): # gas and cost are the same length 
            total += (gas[i] - cost[i]) 

            if total < 0:  
                total = 0 
                res = i + 1   
     
        return res 

            