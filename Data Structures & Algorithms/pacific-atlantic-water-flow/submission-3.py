# reversed the thinking, as we are going from the ocean to the cell
"""
1) we find the dimensions of the grid
2) make two hashsets for visited cells that go on pacifc and atlantic side
3) do a dfs helper func to traverse thru each valid cell at a time 
4) dfs parameter should hold: 
each cell in a row, each cell in a col, visited cell, and the value in a cell
5) Base Cases: if r and c out of bound, run to a cell already visited, or the prev height is bigger than the current height
return None
6) otherwise, it it's in bound, return 
7) now add it in visited 
8) Make a recursion to use later so we can move around down, up, left, right valid cells 
9) now loop thru every row cell 
- call the dfs with your starting position, current c, pac in ur visited object since it's on the top and left side
- call the dfs with your ending position, current c, atl in your visited object since it's on the bottom and right side
10) Loop thru every col cell 
- call the dfs with your current r, starting position, pac in ur visited object since it's on the top and left side
- call the current c, ending position, atl in your visited object since it's on the bottom and right side 
11) Now loop thru the whole graph and append your sublist in your res list
12) return res
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROW, COL = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(r, c, visited, prevHeights):
            if r < 0 or r >= ROW or c < 0 or c >= COL or (r,c) in visited or heights[r][c] < prevHeights:
                return None
            else:
                visited.add((r,c))
                dfs(r-1,c,visited,heights[r][c])
                dfs(r+1,c,visited,heights[r][c])
                dfs(r,c-1,visited,heights[r][c])
                dfs(r,c+1,visited,heights[r][c])
        
        for r in range(ROW):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COL-1,atl,heights[r][COL-1])

        for c in range(COL):
            dfs(0,c,pac,heights[0][c])
            dfs(ROW-1,c,atl,heights[ROW-1][c])

        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res 






        

        