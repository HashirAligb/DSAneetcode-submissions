class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # so im gonna use dfs to go through all the neighbors of my first node and append it to visited 
        # then once t trickles back aka it hit a node not connected 
        # ill exit the dfs and increment my commponents count as well as start a new dfs 
        # this will be done with my outer for loop 
        # essentially my visited set will indicate whether or not im hitting a new node so if i hit a node durong my dfs ill continue 

 
        hashmap = {node : [] for node in range(n)}   
        components = 0 
        visited = set()

        for node1, node2 in edges: 
            hashmap[node1].append(node2) 
            hashmap[node2].append(node1)   # doing this since its an undirected graph  
        
        def dfs(node):  
            for neighbor in hashmap[node]: 
                    if neighbor not in visited: 
                        visited.add(neighbor) 
                        dfs(neighbor) 

        for node in hashmap: 
            if node in visited: 
                continue  
            else: 
                components += 1 
                visited.add(node)  
                dfs(node)
        return components 
        

