class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        edgeMap = {i:[] for i in range(n)} 
        for j, k in edges: 
            edgeMap[j].append(k) 
            edgeMap[k].append(j)   

        visited = set()
        def dfs(i, prev): 
            if i in visited: 
                return False 
            visited.add(i) 
            for j in edgeMap[i]:  
                if j == prev: 
                    continue 
                if not dfs(j, i): return False  
            return True 

        return dfs(0, -1) and len(visited) == n