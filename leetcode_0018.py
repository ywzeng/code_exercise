class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        
        nums.sort()
        result_list = []
        for i in range(len(nums)-3):
            # The data on the right of nums[i] are all greater than nums[i] in the sorted list.
            if target > 0 and nums[i] > target:
                break
            # Pass the duplicate num-pair.
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and (nums[j] == nums[j-1]):
                    continue
                left, right = j+1, len(nums)-1
                while left < right:
                    temp_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if temp_sum == target:
                        result_list += [[nums[i], nums[j], nums[left], nums[right]]]
                        # Pass the duplicate nums.
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif temp_sum < target:
                        left += 1
                    else:
                        right -= 1
        return result_list
