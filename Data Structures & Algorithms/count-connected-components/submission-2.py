class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        edgeMap = {i: [] for i in range(n)} 

        for n1, n2 in edges: 
            edgeMap[n1].append(n2) 
            edgeMap[n2].append(n1) 

        visited = set() 

        def dfs(i): 
            for nei in edgeMap[i]: 
                if nei not in visited: 
                    visited.add(nei) 
                    dfs(nei)

        group = 0 
        for node in range(n): 
            if node in visited: 
                continue 
            else: 
                group += 1
                visited.add(node) 
                dfs(node)  
        return group 



        
    