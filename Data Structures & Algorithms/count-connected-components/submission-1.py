class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
       
        edgeMap = { i : [] for i in range(n) } 

        groups = 0 
        visited = set() 

        for n1, n2 in edges: 
                edgeMap[n1].append(n2) 
                edgeMap[n2].append(n1) 

        def dfs(i):  
            for nei in edgeMap[i]:  
                if nei not in visited:  
                    visited.add(nei)
                    dfs(nei)  

        for node in edgeMap: 
            if node in visited: 
                continue 

            else: 
                visited.add(node) 
                groups += 1 
                dfs(node) 

        return groups  

        
    