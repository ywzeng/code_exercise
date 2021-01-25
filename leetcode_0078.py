class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def back_track(nums: list, begin_index: int, track_list: list, result_list: list) -> None:
            if track_list:
                result_list += [track_list[:]]
            
            for i in range(begin_index, len(nums)):
                track_list += [nums[i]]
                back_track(nums, i+1, track_list, result_list)
                track_list.pop()
        
        track_list, result_list = [], [[]]
        back_track(nums, 0, track_list, result_list)
        return result_list
