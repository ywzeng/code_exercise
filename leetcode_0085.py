class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """ Monotonic Stack """
        if not matrix:
            return 0
        max_area = 0
        prior_height_list = [0 for i in range(len(matrix[0]))]
        for row in range(len(matrix)):
            # Add two sentinels.
            current_height_list = [0] + [int(matrix[row][i])+prior_height_list[i] if int(matrix[row][i])>0 else 0 for i in range(len(matrix[row]))] + [0]
            stack = [0]     # The monotonic stack only records the index of each bar.
            for i in range(1, len(current_height_list)):
                while current_height_list[i] < current_height_list[stack[-1]]:
                    poped_height = current_height_list[stack.pop()]
                    width = i - stack[-1] -1
                    max_area = max(width*poped_height, max_area)
                stack += [i]
            prior_height_list = current_height_list[1:-1]
        return max_area
