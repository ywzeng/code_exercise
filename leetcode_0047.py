"""
Question:
  Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
Two solutions:
  The Solution_stupid is a stupid method, namely applying the backtracking algorithm directly. Store the index of the 'nums' in the track_list.
  A better solution is use pruning during when backtrack the tree. The specific method can refer to Solution_better.
"""


class Solution_better:
    def __init__(self):
        self.result_list = []
        self.check_list = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()      # The elements equal with each other are adjacent in a sorted list.
        self.check_list = [False for i in range(len(nums))]     # Indicate whether the value has been parsed.
        track_list = []      # Store the parsed value.
        self.back_track(nums, track_list)
        return self.result_list
    
    def back_track(self, nums: List[int], track_list: List[int]) -> None:
        if len(track_list) == len(nums):
            temp_list = [i for i in track_list]     # deep copy
            self.result_list += [temp_list]
            return

        for i in range(len(nums)):
            # If the current value has been parsed, continue.
            if self.check_list[i]:
                continue
            # check_list[i-1] is False means that the [i-1] value has been parsed and has been rollback.
            if i > 0 and nums[i] == nums[i-1] and not self.check_list[i-1]:
                continue

            track_list += [nums[i]]
            self.check_list[i] = True
            self.back_track(nums, track_list)
            # Rollback
            track_list.pop()
            self.check_list[i] = False


class Solution_stupid:
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
