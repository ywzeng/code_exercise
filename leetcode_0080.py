class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """ Double pointers. """
        if len(nums) < 3:
            return len(nums)
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right] and right < len(nums)-1:
                right += 1
            else:
                # Handle the duplicate numbers in the tail.
                if nums[left] == nums[right]:
                    right += 1
                # Check the difference between right and left.
                difference = right - left
                while difference > 2:
                    nums.pop(left)
                    difference -= 1
                    right -= 1
                left = right
                right += 1
        return len(nums)
