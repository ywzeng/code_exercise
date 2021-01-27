class Solution_Monotonic_Stack:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """ Monotonic stack. """
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]
        
        max_area = 0
        stack = []
        for i in range(len(heights)):
            # Compare current height with the height of the stack-top element.
            while stack and heights[i] < heights[stack[-1]]:
                poped_height = heights[stack.pop()]
                while stack and poped_height == heights[stack[-1]]:
                    stack.pop()
                width = i if not stack else i-stack[-1]-1
                max_area = max(max_area, poped_height*width)
            stack += [i]
        while stack:
            poped_height = heights[stack.pop()]
            while stack and poped_height == heights[stack[-1]]:
                stack.pop()
            width = len(heights) if not stack else len(heights)-stack[-1]-1
            max_area = max(max_area, poped_height*width)
        
        return max_area



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
