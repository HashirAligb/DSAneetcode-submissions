class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
       # ill have a visited 
       # ill hold a res var which checks all 4 directions 
       # ill remove from set the position to backtrack  
       # my base case will include the word[i] and boardrc being equal  
       # also checking if i succesfully reaches the end of my word   
        rows, cols = len(board), len(board[0])
        visited = set() 
    
        def dfs(r, c, i):   
            if i == len(word): 
                return True 
            
            if (r < 0 or c < 0 or r >= rows or c >= cols 
                or word[i] != board[r][c] or 
                (r,c) in visited  
            ): 
                return False 
            
            visited.add((r,c)) 

            res = ( 
                    dfs(r + 1, c, i + 1) or 
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1)
            )  
            visited.remove((r,c)) 
            return res 

        for r in range(rows): 
            for c in range(cols):
                if dfs(r, c, 0): return True 
        return False

                



          
                        
             
            
