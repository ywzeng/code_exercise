"""
Question:
  Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
Two solutions:
  The Solution_1 is a stupid method, namely applying the backtracking algorithm directly. Store the index of the 'nums' in the track_list.
  A better solution is ...
"""

class Solution_1:
    def __init__(self):
        self.result_list = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        track_list = []     # Only store the index of the elements in nums.
        self.back_track(nums, track_list)
        return self.result_list
    
    def back_track(self, nums: list, track_list: list) -> None:
        if len(track_list) == len(nums):
            temp_list = [nums[i] for i in track_list]
            if temp_list not in self.result_list:
                self.result_list += [temp_list]
            return
        
        for i in range(len(nums)):
            if i in track_list:
                continue
            track_list += [i]
            self.back_track(nums, track_list)
            track_list.pop()
