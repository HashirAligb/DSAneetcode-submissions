class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        res = [] 

        for i, n in enumerate(costs): 
            c1, c2 = n  
            diff = c2 - c1
            res.append([diff, c1, c2]) 
        
        res.sort() 

        total = 0 

        for i in range(len(res)//2):  
            total += res[i][2]
        
        for i in range(len(res)//2, len(res)): 
            total += res[i][1] 
        
        return total
            
            