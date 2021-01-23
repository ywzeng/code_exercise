class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ Binary Search. """
        def binary_search(search_list: list, left: int, right: int, target: int) -> int:
            """ Get the right row / col. """
            if left == right:
                return left
            mid = (left + right) // 2
            if target == search_list[mid]:
                return mid
            elif target < search_list[mid]:
                return binary_search(search_list, left, mid, target)
            else:   # > mid
                if mid+1 <= right and target >= search_list[mid+1]:
                    return binary_search(search_list, mid+1, right, target)
                else:
                    return mid
        
        row_head_elements = [row[0] for row in matrix]
        row_index = binary_search(row_head_elements, 0, len(matrix)-1, target)
        target_row_elements = [data for data in matrix[row_index]]
        col_index = binary_search(target_row_elements, 0, len(matrix[row_index])-1, target)
        return target == matrix[row_index][col_index]
