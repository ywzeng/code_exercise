class Solution_DP:
    def trap(self, height: List[int]) -> int:
        """
        DP
        Use two lists to record the greatest number of corresponding index's two sides.
        left_height_list[i] = max(left_height_list[i-1], height[i-1])
        right_height_list[i] = max(right_height_list[i+1], height[i+1])
        Omit the first and the last number.
        """
        if len(height) < 3:
            return 0
        left_height_list = [0 for i in range(len(height))]
        right_height_list = [0 for i in range(len(height))]
        left_height_list[0] = height[0]
        right_height_list[-1] = height[-1]

        for i in range(1, len(height)-1):
            left_height_list[i] = max(left_height_list[i-1], height[i-1])
        for i in range(len(height)-2, 0, -1):
            right_height_list[i] = max(right_height_list[i+1], height[i+1])
        
        total_water = 0
        for i in range(1, len(height)-1):
            min_height = min(left_height_list[i], right_height_list[i])
            water = min_height-height[i] if min_height > height[i] else 0
            total_water += water
        return total_water


class Solution_stupid:
    def trap(self, height: List[int]) -> int:
        """ 
        Traverse the list form left to right, and get the greatest numbers on its both sides.
        If current number smaller than the lower one of the two greatest numbers, the corresponding index will have water.
        The water volume is the difference between the lower number and it.
        """
        water_list = []
        for i in range(1, len(height)-1):       # Omit the first and the last numbers.
            left_height, right_height = 0, 0
            # Get the greatest number on its left side.
            for j in range(i):
                if height[j] > left_height:
                    left_height = height[j]
            # Get the greatest number on its right side.
            for j in range(i+1, len(height)):
                if height[j] > right_height:
                    right_height = height[j]
            min_height = min(left_height, right_height)
            current_water = min_height-height[i] if min_height > height[i] else 0
            water_list += [current_water]
        return sum(water_list)
