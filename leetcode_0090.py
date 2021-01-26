class Solution_better:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def back_track(nums: int, begin: int, track_list: list, result_list: list) -> None:
            result_list += [track_list[:]]
            
            for i in range(begin, len(nums)):
                if i > begin and nums[i] == nums[i-1]:
                    continue
                track_list += [nums[i]]
                back_track(nums, i+1, track_list, result_list)
                track_list.pop()
        nums.sort()
        track_list, result_list = [], []
        back_track(nums, 0, track_list, result_list)
        return result_list


class Solution_Hash_Map:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        def back_track(nums: list, begin: int, track_list: list, hash_list: list, result_list: list) -> None:
            temp_hash = Counter(track_list)
            if temp_hash in hash_list:
                return

            result_list += [track_list[:]]
            hash_list += [temp_hash]

            for i in range(begin, len(nums)):
                track_list += [nums[i]]
                back_track(nums, i+1, track_list, hash_list, result_list)
                track_list.pop()
        
        track_list, hash_list, result_list = [], [], []
        back_track(nums, 0, track_list, hash_list, result_list)
        return result_list
