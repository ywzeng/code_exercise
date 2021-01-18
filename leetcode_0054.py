class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ Actually, this problem equals to traverse the matrix layer by layer in a clockwise direction. """
        def layer_traverse(matrix: List[List[int]], top: int, left: int, bottom: int, right: int, result_list: List[int]) -> List[int]:
            if left > right or top > bottom:
                return
            # Normal matrix.
            if left < right and top < bottom:
                # top
                for i in range(left, right):
                    result_list += [matrix[top][i]]
                # right
                for i in range(top, bottom):
                    result_list += [matrix[i][right]]
                # bottom
                for i in range(right, left, -1):
                    result_list += [matrix[bottom][i]]
                # left
                for i in range(bottom, top, -1):
                    result_list += [matrix[i][left]]
            # Only one row in the matrix, just traverse it from left to right.
            elif left < right and top == bottom:
                for i in range(left, right+1):
                    result_list += [matrix[top][i]]
            # Only one column in the matrix, just traverse it from top to bottom.
            elif left == right and top < bottom:
                for i in range(top, bottom+1):
                    result_list += [matrix[i][left]]
            # Only one element in the matrix.
            else:
                result_list += [matrix[top][left]]

            layer_traverse(matrix, top+1, left+1, bottom-1, right-1, result_list)
            return

        result_list = []
        layer_traverse(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1, result_list)
        return result_list
