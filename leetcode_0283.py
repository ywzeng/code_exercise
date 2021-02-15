class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Double pointers. Swap the value of two pointers when left is 0 ad right is not 0.
        """
        left, right = 0, 0
        while left < len(nums):
            if nums[left] != 0:
                right = left + 1
            else:
                while right < len(nums) and nums[right] == 0:
                    right += 1
                if right >= len(nums):
                    return
                nums[left], nums[right] = nums[right], nums[left]
            left += 1
