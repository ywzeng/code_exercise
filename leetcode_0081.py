class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binary_search(nums: list, left: int, right: int, target: int) -> bool:
            if left > right or (left == right and nums[left] != target):
                return False
            
            while left+1 < len(nums) and nums[left] == nums[right]:
                left += 1

            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # Left is ordered.
            elif nums[left] < nums[mid] and nums[left] <= target < nums[mid]:
                return binary_search(nums, left, mid, target)
            # Right is ordered.
            elif nums[mid] < nums[right] and nums[mid] < target <= nums[right]:
                return binary_search(nums, mid+1, right, target)
            # Left is disordered.
            elif nums[mid] < nums[left] and (target < nums[mid] or target > nums[right]):
                return binary_search(nums, left, mid, target)
            # Right is disordered.
            elif nums[right] < nums[mid] and (target > nums[mid] or target < nums[left]):
                return binary_search(nums, mid+1, right, target)
            else:
                return False
        
        return binary_search(nums, 0, len(nums)-1, target)
