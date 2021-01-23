class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row_dict, zero_col_dict = {}, {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_row_dict[i] = 1
                    zero_col_dict[j] = 1
        for row in zero_row_dict:
            for j in range(len(matrix[row])):
                matrix[row][j] = 0
        for col in zero_col_dict:
            for i in range(len(matrix)):
                matrix[i][col] = 0
