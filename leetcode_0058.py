class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Omit the spacings in the tail.
        right_index = len(s)-1
        while s[right_index] == ' ':
            right_index -= 1
            if right_index < 0:
                return 0
        
        # Find the last word from tail to head. 
        left_index = right_index
        while left_index >= 0 and s[left_index] != ' ':
            left_index -= 1
        
        return right_index - left_index
