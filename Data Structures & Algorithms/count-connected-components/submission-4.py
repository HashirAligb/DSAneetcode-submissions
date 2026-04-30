class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        groups = 0 

        edgeMap = {i: [] for i in range(n)} 

        for i, j in edges: 
            edgeMap[i].append(j) 
            edgeMap[j].append(i)  

        visited = set()
        def dfs(i): 
            if i in visited: 
                return 
            visited.add(i) 

            for nei in edgeMap[i]: 
                dfs(nei)

        for n in range(n):  
            if n not in visited:  
                groups += 1
                dfs(n)  
        return groups 







