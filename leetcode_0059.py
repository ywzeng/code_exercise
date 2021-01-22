class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """ It must be a square matrix. """
        def clock_wise_parse(square_matrix: list, begin: int, end: int, num: int) -> None:
            if begin > end:
                return
            if begin == end:
                square_matrix[begin][begin] = num
                return
            # Top row.
            for i in range(0, end-begin):
                square_matrix[begin][begin+i] = num
                num += 1
            # Right column.
            for i in range(0, end-begin):
                square_matrix[begin+i][end] = num
                num += 1
            # Bottom row.
            for i in range(0, end-begin):
                square_matrix[end][end-i] = num
                num += 1
            # Left column.
            for i in range(0, end-begin):
                square_matrix[end-i][begin] = num
                num += 1

            # Switch into the next inner layer.
            clock_wise_parse(square_matrix, begin+1, end-1, num)


        square_matrix = [[0 for i in range(n)] for i in range(n)]
        clock_wise_parse(square_matrix, 0, n-1, 1)
        return square_matrix
