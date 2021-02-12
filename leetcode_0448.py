class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            if i > len(nums):
                nums[i%(len(nums))-1] += len(nums)
            else:
                nums[i-1] += len(nums)
        return [i+1 for i in range(len(nums)) if nums[i] <= len(nums)]
