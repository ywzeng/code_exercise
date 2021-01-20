class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        The key point of this problem is the negative integers.
        We cannot directly take the greatest three numbers. We should consider the smallest three numbers when there are negative integers.
        """
        nums.sort()
        max_num = 0
        if nums[1] < 0:
            max_num = nums[0]*nums[1]*nums[-1]
        return max(max_num, nums[-1]*nums[-2]*nums[-3])
