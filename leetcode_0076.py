class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """ 
        Do not forget the duplicate of target characters in target string 't'. 
        Move the right pointer untill find all target characters
        """
        from collections import Counter
        window_map = Counter()      # record the target characters in the sliding window.
        target_map = Counter(t)

        left, right = 0, -1
        min_length = len(s) + 1     # The length of the shortest target substring.
        min_left_index = 0      # Record the index of the sortest target substring.

        while right < len(s)-1:
            right += 1
            # Find a target character.
            if right < len(s) and s[right] in target_map:
                window_map[s[right]] += 1

            # Check whether have collected enough target characters.
            has_enough = True
            for key in target_map:
                if window_map[key] < target_map[key]:
                    has_enough = False
                    break

            # Already find all the target characters, move the left pointer to filter the irrelevant characters.
            if has_enough:
                # Filter the irrelevant characters.
                while (left < right and s[left] not in target_map) or (s[left] in target_map and window_map[s[left]] > target_map[s[left]]):
                    if s[left] in window_map:
                        window_map[s[left]] -= 1
                    left += 1
                if right+1-left < min_length:
                    min_length = right+1-left
                    min_left_index = left
                
                # Further move the left pointer to get the next target substring.
                window_map[s[left]] -= 1        # Update the characters in sliding window.
                left += 1
        return s[min_left_index:min_left_index+min_length] if min_length <= len(s) else ''
