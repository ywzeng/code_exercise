class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return
        
        def binary_search_recursion(nums: List[int], left: int, right: int, target: int) -> int:
            if left == right:
                return left
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binary_search_recursion(nums, left, mid, target)
            else:
                return binary_search_recursion(nums, mid+1, right, target)

        return binary_search_recursion(nums, 0, len(nums), target)
