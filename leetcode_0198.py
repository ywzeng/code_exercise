class Solution_Better:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        dp_list = [0 for i in nums]
        dp_list[0], dp_list[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp_list[i] = max(dp_list[i-2]+nums[i], dp_list[i-1])
        return dp_list[-1]
    

class Solution_Stupid:
    def rob(self, nums: List[int]) -> int:
        """
        DP. The interval between two indexes could be greater than 2. Actualy, two step plans: 1 or 2.
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp_list = [0 for i in nums]
        dp_list[0], dp_list[1] = nums[0], nums[1]
        for i in range(2, len(nums)):
            if i > 2:
                dp_list[i] = nums[i] + max(dp_list[i-2], dp_list[i-3])
            else:
                dp_list[i] = nums[i] + dp_list[i-2]
        return max(dp_list[-1], dp_list[-2])
