# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0003.py
@time: 2021/1/11
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Use two indexes, i and j, to form a sliding window.
        If s[j] exists in s[i: j], there are duplicate characters. We Record the length of the current sliding window.
        Then turn the index 'i' to (index+1) of the duplicated character in s[i: j], and reset the index 'j' to 'i'.
        """
        s_len = len(s)
        if s_len < 2:
            return s_len

        i, j = 0, 1
        max_length = j - i
        while j < s_len:
            # Expand the sliding window
            if s[j] not in s[i: j]:
                j += 1
                continue
            # Encounter the duplicate characters.
            max_length = (j - i) if (j - i) > max_length else max_length
            duplicate_num_index = s[i:j].index(s[j]) + i
            i = duplicate_num_index + 1
            j += 1
        max_length = (j - i) if (j - i) > max_length else max_length
        return max_length
