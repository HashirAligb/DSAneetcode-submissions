class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # make them Ts 
        # make every o x's 
        # make all the ts back to 0s 
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(r, c):  
            if (r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited or board[r][c] != "O"):
                return 

            visited.add((r,c))
            board[r][c] = "T" 
            dfs(r + 1, c) 
            dfs(r - 1, c) 
            dfs(r, c + 1) 
            dfs(r, c - 1)  
        
        for r in range(rows): 
            for c in range(cols): 
                if (r in [0, rows -1] or c in [0, cols - 1] and board[r][c] == "O"): 
                    dfs(r, c) 

        for r in range(rows): 
            for c in range(cols):  
                if board[r][c] == "O": 
                    board[r][c] = "X" 
                if board[r][c] == "T":
                    board[r][c] = "O" 
        

