class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) < 2:
            return
        
        def recursion_rotate(matrix, start, num) -> None:
            """
            The start indicate the top-left index of the matrix [start, start].
            The num indicates the row-num or col-num of the sub-matrix.
            In each recursion, we only rotate the outermost layer of the matrix.
            """
            if num < 2:
                return
            end = start+num-1     # The bottom-right index of the matrix.
            for i in range(num-1):
                temp_element = matrix[start][start+i]
                matrix[start][start+i] = matrix[end-i][start]       # The first col -> the first row.
                matrix[end-i][start] = matrix[end][end-i]       # The last row -> the first col.
                matrix[end][end-i] = matrix[start+i][end]       # The last col -> the last row.
                matrix[start+i][end] = temp_element     # The first row -> the last col.
            
            # Rotate the next inner layer of the matrix, which is the also the outermost layer of the inner sub-matrix.
            recursion_rotate(matrix, start+1, num-2)       # Remove the outermost layer elements
        
        recursion_rotate(matrix, 0, len(matrix))
