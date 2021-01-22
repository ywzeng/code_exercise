class Solution_stupid:
    def getPermutation(self, n: int, k: int) -> str:
        def back_track(n: int, track_list: list, result_list: list, k: int) -> bool:
            if len(track_list) == n:
                result_list += [''.join([str(d) for d in track_list])]
                if len(result_list) == k:
                    return True
                else:
                    return False
            
            for i in range(1, n+1):
                if i in track_list:
                    continue
                track_list += [i]
                has_arrive_k = back_track(n, track_list, result_list, k)
                if has_arrive_k:
                    return True
                track_list.pop()
            return False
        
        track_list, result_list = [], []
        back_track(n, track_list, result_list, k)
        return result_list[-1]          
