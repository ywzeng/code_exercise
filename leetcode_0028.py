class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Find the index of the character that first matches needle[0].
        base_index = 0
        while base_index < len(haystack)-len(needle)+1:
            if haystack[base_index] == needle[0]:
                move_index = base_index+1
                is_matched = True
                for i in range(1, len(needle)):
                    if haystack[move_index+i-1] != needle[i]:
                        is_matched = False
                        break
                if is_matched:
                    break
            base_index += 1
        if base_index >= len(haystack)-len(needle)+1:
            return -1
        return base_index
