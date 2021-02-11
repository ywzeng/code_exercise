class Solution_Hash_Table:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        num_counter = Counter()
        for num in nums:
            num_counter[num] += 1
            if num_counter[num] > len(nums) // 2:
                return num

            
class Solution_Sort:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
