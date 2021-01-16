class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        base_index = 0
        for move_index in range(1, len(nums)):
            if nums[move_index] != nums[base_index]:
                base_index += 1
                nums[base_index] = nums[move_index]     # nums[:base_index] are de-duplicated nums
        return base_index+1
