class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None: 
        q = deque()   
        visited = set()
        rows, cols = len(grid), len(grid[0]) 

        for r in range(rows): 
            for c in range(cols):  
                if grid[r][c] == 0: 
                    visited.add((r,c))  
                    q.append((r,c))  
        def bfs(r, c): 
            if (r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited 
                or grid[r][c] == -1): 
                    return  
            grid[r][c] = dist  
            visited.add((r,c))  
            q.append((r,c))

        dist = 1 
        while q: 
            for i in range(len(q)):  
                r, c = q.popleft() 
                bfs(r, c + 1) 
                bfs(r, c - 1) 
                bfs(r + 1, c) 
                bfs(r - 1, c)  
            dist += 1 
        

                

