class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        edgemap = defaultdict(list) 


        for i, j in edges: 
            edgemap[i].append(j) 
            edgemap[j].append(i) 


        visited = set()
        def dfs(node, prev): 
            if node in visited: 
                return False  
            
            visited.add(node) 

            for nei in edgemap[node]:
                if nei == prev: 
                    continue  
                if not dfs(nei, node): return False 
            
            return True 
        
        return dfs(0, -1) and len(visited) == n 

