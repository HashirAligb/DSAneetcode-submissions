class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited, cycle = set(), set() 
        crsMap = {i: [] for i in range(numCourses)} 

        for crs, pre in prerequisites: 
            crsMap[crs].append(pre) 

        res = []
        def dfs(crs): 
            if crs in visited: 
                return True 
            if crs in cycle:  
                return False 
            
            cycle.add(crs) 
            for pre in crsMap[crs]:  
                if not dfs(pre): return False 
            
            cycle.remove(crs) 
            visited.add(crs)  
            res.append(crs) 
            return True 
        
        for i in range(numCourses): 
            if not dfs(i): 
                return [] 
        return res 



            