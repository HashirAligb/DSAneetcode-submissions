# to get each sub-boxes, i do (row // 3)(col // 3)
# row and column can't contain any duplicates, do i do set?
# edge case: "."

import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROW = defaultdict(set)
        COL = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in ROW[r] or
                    board[r][c] in COL[c] or
                    board[r][c] in square[(r // 3, c // 3)]):
                    return False

                ROW[r].add(board[r][c])
                COL[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        return True


    







        


        