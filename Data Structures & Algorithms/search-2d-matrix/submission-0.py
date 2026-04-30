class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, columns = len(matrix), len(matrix[0]) 

        for i in range(rows): 
            for j in range(columns): 
                if matrix[i][j] == target: 
                    return True 
        return False 
        