class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while True:
            if i + nums[i] >= len(nums)-1:
                return True
            if nums[i] == 0:
                return False
            # Greedily get the next step.
            nest_step_index = i+1
            furthest_distance = 0
            for j in range(i+1, i+nums[i]+1):
                if j + nums[j] >= furthest_distance:
                    nest_step_index = j
                    furthest_distance = j+nums[j]
            i = nest_step_index
