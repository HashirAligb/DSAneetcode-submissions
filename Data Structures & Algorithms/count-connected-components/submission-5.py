class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        edgemap = defaultdict(list) 


        for i, v in edges: 
            edgemap[i].append(v) 
            edgemap[v].append(i) 
        
        visited = set() 

        def dfs(node):  
            if node in visited: 
                return  
            
            visited.add(node) 
            for nei in edgemap[node]: 
                dfs(nei) 
            
            return 

        res = 0 
        for i in range(n): 
            if i not in visited: 
                dfs(i) 
                res += 1  
        return res 
