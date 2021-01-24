class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """ 
        Combination. 
        C(n)(m),  given m numbers, randomly select n numbers from them.
        Combination does not consider the order of the selected numbers.
        Thus, we can use set to sort the selected numbers.
        """
        def back_track(n: int, current_num: int, k: int, track_list: list, result_list: list) -> None:
            if len(track_list) == k:
                result_list += [track_list[:]]
                return
            
            for i in range(current_num, n+1):
                track_list += [i]
                back_track(n, i+1, k, track_list, result_list)
                track_list.pop()
        
        track_list, result_list = [], []
        back_track(n, 1, k, track_list, result_list)
        return result_list
