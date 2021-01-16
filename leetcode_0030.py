from collections import Counter

class Solution_hash_map:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """ Hash Map """
        if not s or not words:
            return []
        
        word_len = len(words[0])        # All words have the same length.
        substring_len = word_len * len(words)
        word_map = Counter(words)       # key is the word, value is the quantity
        result_list = []
        for i in range(len(s) - substring_len + 1):
            current_substring = s[i: i+substring_len]
            temp_str_list = []
            for j in range(0, len(current_substring), word_len):
                temp_str_list += [current_substring[j: j+word_len]]
            if Counter(temp_str_list) == word_map:
                result_list += [i]
        return result_list
