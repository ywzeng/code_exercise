class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        DP, O(n).
        Determine whether the maximum subarray of nums[i:j] is nums[i:j-1] or nums[:j].
        This depends on whether nums[j] will increase the summation of subarray nums[i:j].
        So, dp[i] = max(nums[i], dp[i-1], dp[i-1]+nums[i])
        """
        if len(nums) < 2:
            return nums[0]
        dp = [0 for i in nums]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            # Only positive number will increase the summation of subarray.
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)
