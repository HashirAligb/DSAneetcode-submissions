class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # so ill have two sets pac and atl 
        # ill go through the first row to get all the pacific  
        # and ill go through the last column to get all the atlantic 
        # whichever are borth ill add to my res at the end 
        # ill be calling dfs to add specifc nodes like top left right bottom 
        # in my dfs im gona check if the previous height is LESS cuz from the  
        # two borders anything more means you can go to it so if not ill return 

        #first i will go through top and bottom then left and right borders 


        pac, atl = set(), set() 
        ROW, COL = len(heights), len(heights[0]) 

        def dfs(r, c, visit, prevheight): 
            if ( (r,c) in visit or r < 0 or c < 0 or r == ROW or c == COL  
                or prevheight > heights[r][c]): 
                    return 
            visit.add((r,c))  
            dfs(r + 1, c, visit, heights[r][c]) 
            dfs(r - 1, c, visit, heights[r][c]) 
            dfs(r, c + 1, visit, heights[r][c])  
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COL): # top and bottom border
            dfs(0, c, pac, heights[0][c])   
            dfs(ROW - 1, c, atl, heights[ROW - 1][c])  
        
        for r in range(ROW): # left and right border 
            dfs(r, 0, pac, heights[r][0]) 
            dfs(r, COL - 1, atl, heights[r][COL -1])   

        
        res = []
        
        for r in range(ROW): 
            for c in range(COL): 
                if (r,c) in pac and (r,c) in atl: 
                    res.append([r,c]) 
        return res 



