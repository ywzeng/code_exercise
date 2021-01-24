class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_dict = {0: 0, 1: 0, 2: 0}
        for i in nums:
            temp_dict[i] += 1
        nums[:] = [0]*temp_dict[0] + [1]*temp_dict[1] + [2]*temp_dict[2]
