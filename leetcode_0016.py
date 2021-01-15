class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        base_sum = sum(nums[:3])
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                if abs(target - temp_sum) < abs(target - base_sum):     # update base_sum
                    base_sum = temp_sum
                # If the sum less than the target value, right-move the left pointer to get bigger value, so as to increase the sum to get closer to the target.
                if temp_sum < target:
                    left += 1
                # If the sum greater than the target value, left-move the right pointer to get smaller value, so as to decrease the sum to get closer to the target. 
                elif temp_sum > target:
                    right -= 1
                # The closest, zero distance away from the target.
                else:
                    return base_sum
        return base_sum
