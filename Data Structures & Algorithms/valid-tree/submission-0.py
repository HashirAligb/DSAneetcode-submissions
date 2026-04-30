class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # easy just keep track of prevv by passing i which is my adj list main dude 
        # and j which is the neighbors im looping over  
        # also ill use a visit set to see if ive alr visited the node 
        # undirected so i gott have n1 and n2 

        hashmap = {i : [] for i in range(n)}  
        
        for n1, n2 in edges: 
            hashmap[n1].append(n2) 
            hashmap[n2].append(n1) 
        
        visited = set()
        def dfs(node, prev): 
            if node in visited: 
                return False 
            visited.add(node) 

            for j in hashmap[node]: 
                if j == prev: 
                    continue 
                if not dfs(j, node): 
                    return False  
            return True 
        return dfs(0, -1) and n == len(visited)