class Solution_stupid_enum_width_timeout:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for left in range(len(heights)):       # Enumerate the left index.
            min_height = float('inf')
            for right in range(left, len(heights)):        # Enumerate the right index.
                min_height = min(min_height, heights[right])
                max_area = max(max_area, (right-left+1)*min_height)
        return max_area

    
class Solution_stupid_enum_height_timeout:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            temp_height = heights[i]
            # Find the left border,
            left = i
            while left-1 >= 0 and heights[left-1] >= temp_height:
                left -= 1
            # Find the right border.
            right = i
            while right+1 < len(heights) and heights[right+1] >= temp_height:
                right += 1
            max_area = max(max_area, (right-left+1)*temp_height)
        return max_area
