class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def back_track(candidates: list, begin: int, track_list: list, current_target: int, result_list: list, label_list: list) -> None:
            """ The candidates and current_target are varying during the searching. """
            if current_target == 0:
                temp_list = [num for num in track_list]
                result_list += [temp_list]
                return
            
            for i in range(begin, len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1] and label_list[i-1] == 0:
                    continue
                if current_target < candidates[i]:
                    break
                residue = current_target - candidates[i]
                track_list += [candidates[i]]
                label_list[i] = 1
                # candidates[i+1:], which exculdes the current selected candidates[i].
                back_track(candidates, i+1, track_list, residue, result_list, label_list)
                track_list.pop()
                label_list[i] = 0

        candidates.sort()
        track_list, result_list = [], []
        # Indicate whether the prior candidate have been used before.
        label_list = [0 for i in range(len(candidates))]
        back_track(candidates, 0, track_list, target, result_list, label_list)
        return result_list
