from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        rowsMap = defaultdict(set)
        colsMap = defaultdict(set)
        boxMap = defaultdict(set) 

        rows = len(board) 
        cols = len(board[0]) 

        for r in range(rows): 
            for c in range(cols):  
                if board[r][c] == ".": 
                    continue
                if board[r][c] in rowsMap[r] or board[r][c] in colsMap[c] or board[r][c] in boxMap[(r//3,c//3)]:
                    return False  
                rowsMap[r].add(board[r][c]) 
                colsMap[c].add(board[r][c]) 
                boxMap[(r//3, c//3)].add(board[r][c]) 

        return True 
                