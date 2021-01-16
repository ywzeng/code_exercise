class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if nums_len < 2:
            return
        left, right = nums_len-2, nums_len-1
        # Find the number that is less than its right one, which means that swap it with a greater number on its right will get a greater num-sequence.
        while left >= 0 and nums[left] >= nums[right]:
            left -= 1
            right -= 1
        
        # Current num-sequence is the greatest.
        if left < 0:
            nums.reverse()
            return

        greater_index = nums_len-1
        while greater_index > left:
            if nums[greater_index] > nums[left]:
                break
            greater_index -= 1
        nums[left], nums[greater_index] = nums[greater_index], nums[left]
        # Reverse nums[right:] to the asscending order.
        j = 1
        for i in range(right, right+(nums_len-right)//2):
            nums[i], nums[nums_len-j] = nums[nums_len-j], nums[i]
            j += 1
