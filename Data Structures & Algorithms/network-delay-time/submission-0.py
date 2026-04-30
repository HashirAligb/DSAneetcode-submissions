class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # so im gonna implemet djikstras with a heap, ill use a heap with tuples 
        # these tuples will have the weight, and the nodes for each node in my times list 
        # the reason im gonna do this is because with dikkkstras ill keep popping the minum path 
        # so once ive explored all the paths, ill lastly be left with my maximum path and therefore  
        # my set should have all the nodes, and t would then lastly be updated to the max path 


        paths = defaultdict(list) 
        for u, v, w in times: 
            paths[u].append((v,w)) 
        

        visited = set() 
        t = 0 
        minheap = [(0,k)] 

        while minheap:   
            w1, n1 = heapq.heappop(minheap) 
            if n1 in visited: 
                continue 
            
            visited.add(n1)  
            t = w1 
            
            for n2, w2 in paths[n1]:   
                if n2 not in visited: 
                    heapq.heappush(minheap, (w1 + w2, n2))

        return t if len(visited) == n else -1
            
            
