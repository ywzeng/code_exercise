class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Use XOR.
        a^a=0; a^a^b=b.
        """
        xor_result = nums[0]
        for i in range(1, len(nums)):
            xor_result ^= nums[i]
        return xor_result
