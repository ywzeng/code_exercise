class Solution_Set:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        set_original = set(nums)
        set_full = set(range(1, len(nums)+1))
        return list(set_full - set_original)


class Solution_Index:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            if i > len(nums):
                nums[i%(len(nums))-1] += len(nums)
            else:
                nums[i-1] += len(nums)
        return [i+1 for i in range(len(nums)) if nums[i] <= len(nums)]
