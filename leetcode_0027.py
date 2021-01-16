class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        # Get the index of the data that first matches 'val'.
        base_index = 0
        while base_index < len(nums):
            if nums[base_index] == val:
                break
            base_index += 1
        
        for move_index in range(base_index+1, len(nums)):
            if nums[move_index] != val:
                nums[base_index] = nums[move_index]     # No target 'val' in nums[:base_index+1] .
                base_index += 1
        return base_index
