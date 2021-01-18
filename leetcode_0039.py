class Solution_quick:
    """ Conver the sum operation to minus would save much more time in this question. """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def back_track(candidates: list, track_list: list, target: int, result_list: list) -> None:
            """ The parameter 'target' will be minused by the numbers that appended into the track_list. """
            if target == 0:
                temp_list = [num for num in track_list]
                result_list += [temp_list]
                return
            for i, num in enumerate(candidates):
                if num > target:
                    break
                residue = target - num
                track_list += [num]
                back_track(candidates[i:], track_list, residue, result_list)
                track_list.pop()
        
        candidates.sort()
        result_list, track_list = [], []
        back_track(candidates, track_list, target, result_list)
        return result_list


class Solution_slow:
    """ The sum operation of the list really affect the efficiency. """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def back_track(candidates: List[int], track_list: List[int], target: int, result_list: List[int]) -> None:
            if target < candidates[0] or sum(track_list) > target:
                return
            if sum(track_list) == target:
                temp_list = [num for num in track_list]
                result_list += [temp_list]
                return
            for i, num in enumerate(candidates):
                if num > target:
                    continue
                track_list += [num]
                # Ignore the prior processed candidate in the same layer.
                # Understanding why use candidates[i:].
                back_track(candidates[i:], track_list, target, result_list)
                track_list.pop()
        
        result_list = []
        track_list = []
        candidates.sort()
        back_track(candidates, track_list, target, result_list)
        return result_list
