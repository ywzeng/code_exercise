class Solution_stupid_timeout:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for left in range(len(heights)):       # Enumerate the left index.
            min_height = float('inf')
            for right in range(left, len(heights)):        # Enumerate the right index.
                min_height = min(min_height, heights[right])
                max_area = max(max_area, (right-left+1)*min_height)
        return max_area
