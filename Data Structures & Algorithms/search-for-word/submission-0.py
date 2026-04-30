class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # im just going to recursiveky go through rows and cols to get every single combination 
        # using backtracking, if I see that i already went through a cell, or im out of bounds, or my val in the cell is wrong 
        # ill just return false as my base case  
        # in the end ill loop through the rows and cols to recusrively check every positio 
        # very similar to number of islands 

        ROWS, COLS = len(board), len(board[0])  
        visited = set()  

        def dfs(r, c, i):  
            if i == len(word): 
                return True      #means we reached an ending combination 
            if (r < 0 or c < 0 or 
            r >= ROWS or c >= COLS or  
            word[i] != board[r][c] or
            (r,c) in visited): 
                return False   
            
            visited.add((r, c)) # so we found a valid point 
            # now ill explore all four sides and also increment my i which is my iterator
            res =   (dfs(r + 1, c, i + 1) or 
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1)) 
            # i casted these in a res so itll return if any of these ways got a valid combo  
            # ill remove my starting point now from visited so it can be used for other combos 

            visited.remove((r,c))  
            return res  
        
        for r in range(ROWS): 
            for c in range(COLS): 
                if dfs(r, c, 0): return True 
        return False 


                        
             
            
