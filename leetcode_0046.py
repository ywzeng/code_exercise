class Solution:
    def __init__(self):
        self.result_list = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        track_list = []     # Store the already parsed numbers.
        self.back_track(nums, track_list)
        return self.result_list

    def back_track(self, nums: list, track_list: list) -> None:
        # Already parsed all the numbers.
        if len(track_list) == len(nums):
            temp_list = [i for i in track_list]     # shallow copy
            self.result_list += [temp_list]
            return
        
        for num in nums:
            if num in track_list:
                continue
            track_list += [num]
            self.back_track(nums, track_list)
            track_list.pop()
