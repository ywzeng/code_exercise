class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        def binary_search(nums: List[int], left: int, right: int, target: int) -> int:
            if target > nums[right] or target < nums[left]:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return binary_search(nums, left, mid, target)
            else:
                return binary_search(nums, mid+1, right, target)

        target_index = binary_search(nums, 0, len(nums)-1, target)
        if target_index == -1:
            return [-1, -1]
        # Find the start index of the target.
        start_index = target_index
        while start_index >= 0 and nums[start_index] == target:
            start_index -= 1
        start_index += 1
        # Find the end index of the target.
        end_index = target_index
        while end_index <= len(nums)-1 and nums[end_index] == target:
            end_index += 1
        end_index -= 1
        return [start_index, end_index]
