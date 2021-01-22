class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        def back_track(n: int, track_list: list, result_list: list, k: int) -> bool:
            if len(track_list) == n:
                temp_list = [d for d in track_list]
                result_list += [temp_list]
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
        
        # Pre-calculate the sub-tree index of the k-th leaf node.
        start_index = 0
        for i in range(1, n):
            if factorial(n-1)*i >= k:
                break
            start_index += 1

        track_list = [start_index+1] if start_index > 0 else []
        result_list = []
        back_track(n, track_list, result_list, k-factorial(n-1)*start_index)
        return ''.join([str(d) for d in result_list[-1]])
