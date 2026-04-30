class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # so the main diff between this question and the first version is 
        # ill use two hashsets this time bc i want to know if theres a cycle 
        # ill return false if my crs is alr in the cycle set, otherwirse ill add to it 
        # once ive gone through all pre reqs thru dfs and all of them return true ill 
        # add my crs to the output, bc its essentially passed adn had all its, prereq crs added 
        # to the output alr, so basically the first output crs will be the one wiht no pre req  
        # but if a crs has a pre req and i saw that pre req already that means i have to return false 

        hashmap = {n : [] for n in range(numCourses)} 
        for crs, pre in prerequisites: 
            hashmap[crs].append(pre) 
        output = []
        visit = set() 
        cycle = set()
        def dfs(crs): 
            if crs in visit: 
                return True 
            if crs in cycle:  
                return False 
            
            cycle.add(crs)
            
            for i in hashmap[crs]: 
                if dfs(i) == False: 
                    return False  
            cycle.remove(crs)   
            visit.add(crs) 
            output.append(crs)  
            return True  
        for i in range(numCourses): 
            if dfs(i) == False: 
                return [] 
        return output