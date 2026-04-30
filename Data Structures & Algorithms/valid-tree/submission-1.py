class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # easy just keep track of prevv by passing i which is my adj list main dude 
        # and j which is the neighbors im looping over  
        # also ill use a visit set to see if ive alr visited the node 
        # undirected so i gott have n1 and n2 

        adjList = {i : [] for i in range(n)} 

        for n1, n2 in edges: 
            adjList[n1].append(n2) 
            adjList[n2].append(n1)
             
        visit = set() 

        def dfs(i, prev):  
            if i in visit: 
                return False  
            visit.add(i)
            for node in adjList[i]: 
                if node == prev: 
                    continue 
                if not dfs(node, i): return False 
            return True 
        
        return dfs(0, -1) and len(visit) == n


        