class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        num_sum = sum(nums)
        left_sum = 0
        index = -1
        for i in range(len(nums)):
            if left_sum * 2 + nums[i] == num_sum:
                index = i
                break
            left_sum += nums[i]
        return index
