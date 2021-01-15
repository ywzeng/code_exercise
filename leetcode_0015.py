class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """  """
        if not nums or len(nums) < 3:
            return []

        nums.sort()
        result_list = []
        for i in range(len(nums)-2):
            if nums[i] > 0:     # The numbers on the right of nums[i] are all greater than it.
                break
            if i > 0 and nums[i] == nums[i-1]:      # pass the duplicate numbers.
                continue
            left, right = i+1, len(nums)-1      # left & right pointers.
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if temp_sum == 0:
                    result_list += [[nums[i], nums[left], nums[right]]]
                    while left < right and nums[left] == nums[left+1]:      # pass the duplicate numbers.
                        left += 1
                    while left < right and nums[right] == nums[right-1]:        # pass the duplicate numbers.
                        right -= 1
                    left += 1
                    right -= 1
                # Sum less than 0 indicates that the left-pointer-number is small, we should right-move the left-pointer to get a bigger number.
                elif temp_sum < 0:
                    left += 1
                # Sum greater than 0 indicates that the right-pointer-number is big, we should left-move the right-pointer to get a smaller number.
                else:
                    right -= 1
        return result_list
