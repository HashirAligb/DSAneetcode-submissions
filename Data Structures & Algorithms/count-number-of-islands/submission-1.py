"""
col is going left and right
row is going up and down
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        visited = set()
        row = len(grid)
        col = len(grid[0])
        count = 0

        def dfs(r, c):
            if 0 > r or r >= row or 0 > c or c >= col or grid[r][c] != "1":
                return None 
            else:
                grid[r][c] = "0"
                dfs(r - 1, c)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
                    visited.add((r,c))  

        return count


                
        
        