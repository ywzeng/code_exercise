class Solution_Rotate:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_func(nums: list, start: int, end: int) -> list:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            return nums
        k %= len(nums)
        nums[:] = reverse_func(nums, 0, len(nums)-1)
        nums[:] = reverse_func(nums, 0, k-1)
        nums[:] = reverse_func(nums, k, len(nums)-1)

class Solution_Trash:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
