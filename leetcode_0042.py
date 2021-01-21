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
