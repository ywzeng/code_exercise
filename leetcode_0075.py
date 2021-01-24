class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Two pointers, one for '0' and another for '2'.
        In specific, if nums[i] == 0, swap it with p_0; if nums[i] == 2, swap it with p_2.
        The remaining part is '1'.
        """
        i, p0, p2 = 0, 0, len(nums)-1
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
                i -= 1
            i += 1
        return nums


class Solution_meaningless:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_dict = {0: 0, 1: 0, 2: 0}
        for i in nums:
            temp_dict[i] += 1
        nums[:] = [0]*temp_dict[0] + [1]*temp_dict[1] + [2]*temp_dict[2]
