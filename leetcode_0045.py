class Solution:
    def jump(self, nums: List[int]) -> int:
        current_index = 0
        hop = 0
        while current_index < len(nums)-1:
            if current_index + nums[current_index] >= len(nums)-1:
                hop += 1
                break
            candidate_step_list = nums[current_index+1: current_index+nums[current_index]+1]
            # The best nest step-index should be the nearst from the tail.
            nearest_step, nearest_step_index = candidate_step_list[0], 0
            for i in range(1, len(candidate_step_list)):
                if candidate_step_list[i]+i >= nearest_step+nearest_step_index:
                    nearest_step = candidate_step_list[i]
                    nearest_step_index = i
            current_index += nearest_step_index+1
            hop += 1
        return hop
