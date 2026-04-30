class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) 
        q = deque() 
        fresh = 0 

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1: 
                    fresh += 1 
                if grid[r][c] == 2: 
                    q.append((r,c)) 
        
        def bfs(r, c): 
            nonlocal fresh  
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1): 
                return  

            grid[r][c] = 2  
            q.append((r,c))
            fresh -= 1 
        
        minutes = 0 
        while q and fresh > 0: 
            for i in range(len(q)):
                r, c = q.popleft()  
                bfs(r + 1, c) 
                bfs(r - 1, c) 
                bfs(r, c + 1) 
                bfs(r, c - 1)   
            minutes += 1
            
        return minutes if fresh == 0 else -1 
            








                


