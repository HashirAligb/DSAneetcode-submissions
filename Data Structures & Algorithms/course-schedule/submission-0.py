class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # ok to simulate the graph ill create a hashmap where ill have the num courses map to their respective prereqs 
        # also i wanna check with a visit set whether a course has been visited thus returning false. 
        # however if every course in my hashmap at that nnum course passes the conditions i can remove it from visit set 
        # and also i can set the pre reqs to and empty set for it to pass my conditions and complete the ovcerall dfs 
        # also in the end i have to loop through all the courses because there is a potential chance where my courses are not 
        # connected   

        hashmap = {i : [] for i in range(numCourses)}
        visit = set()  

        for crs, prereq in prerequisites: 
            hashmap[crs].append(prereq)  # mapping everything together 

        def dfs(crs):  
            if crs in visit: 
                return False 
            if hashmap[crs] == []: 
                return True 
            
            visit.add(crs) 
            for i in hashmap[crs]: 
                if not dfs(i): return False # call dfs on all 
            visit.remove(crs) # clear it if it passes the conditions 
            hashmap[crs] = []  
            return True
        
        for c in range(numCourses): 
            if not dfs(c): return False 
        return True 

