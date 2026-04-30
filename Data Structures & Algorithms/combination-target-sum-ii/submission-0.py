class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #ill do my backtracking tree after sorting, to get all combinations 
        # to keep my combinations distinct ill pass a while loop in before my second 
        # dfs call so that it continues till i is changed 
     

        candidates.sort() 
        res = [] 
        
        def dfs(i, curr, total): 
            if total == target: 
                res.append(curr.copy()) #first base case if we get a valid combo 
                return 
            if total > target or i == len(candidates): 
                return 
            
            curr.append(candidates[i]) 

            dfs(i+1, curr, total + candidates[i]) 
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]: 
                i += 1  
            
            dfs(i + 1, curr, total)    

        dfs(0, [], 0) 
        
        return res 

            
