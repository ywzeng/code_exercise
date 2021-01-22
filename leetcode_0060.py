class Solution_clever:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Divide n! into n partation, each contains (n-1)! sub-permutations.
        Iteratively do this divide from n to 1.
        """
        from math import factorial
        if n == 1:
            if k == 1:
                return str(n)
            else:
                return ''
        k -= 1
        candidate_element = [i for i in range(1, n+1)]
        result = []
        while n > 0:
            temp_factorial = factorial(n-1)
            n_temp_index = k // temp_factorial      # Choose the right high bit of the k-th permutation.
            result += [str(candidate_element[n_temp_index])]
            # Update the candidate elements and k.
            candidate_element = candidate_element[:n_temp_index] + candidate_element[n_temp_index+1:]
            k -= n_temp_index * temp_factorial
            n -= 1

        return ''.join(result)


class Solution_back_track:
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
