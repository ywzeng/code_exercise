class Solution_Moore_Voting:
    def majorityElement(self, nums: List[int]) -> int:
        mode = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == mode:
                count += 1
            else:
                count -= 1
                if count == 0:
                    mode = nums[i+1]
        return mode

    
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
