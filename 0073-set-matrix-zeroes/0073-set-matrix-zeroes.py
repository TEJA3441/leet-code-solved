from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(m))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(n))
        
        # Use first row and first column to mark zeros
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out cells based on markers
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out first row if needed
        if first_row_has_zero:
            for j in range(m):
                matrix[0][j] = 0
        
        # Zero out first column if needed
        if first_col_has_zero:
            for i in range(n):
                matrix[i][0] = 0
