class Solution_stupid_hash_map:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        hash_map_list = []
        result_list = []
        for temp_str in strs:
            hash_str = Counter(temp_str)
            has_matched = False
            for i, hash_map in enumerate(hash_map_list):
                if hash_map == hash_str:
                    result_list[i] += [temp_str]
                    has_matched = True
                    break
            if not has_matched:
                hash_map_list += [hash_str]
                result_list += [[temp_str]]
        return result_list
