# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0005.py
@time: 2021/1/12
"""

"""
Solution_1 uses DP. But the time complexity of this method is O(n^2).
We can employ another method to solve this problem, which depends on the unique characteristics of the palindromic string.
"""


class Solution_1:
    def longestPalindrome(self, s: str) -> str:
        """
        A palindromic string 'S' refers to  S==S.reverse().
        Note that, the substring of a palindromic string is a palindromic string as well.
        Namely, if s[i: j] is a palindromic string, s[i+1: j-1] is also a palindromic string.
        Therefore, a string s[i: j] is a palindromic string if and only if s[i+1: j-1] is a palindromic string and s[i] == s[j].
        """
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]

        max_len = 1
        max_substring = s[0]
        # Form a State Transition Matrix with default 'False' value.
        t_matrix = [[False for i in range(len(s))] for i in range(len(s))]
        # Set the value of matrix[i][i] (s[i]) to True.
        for i in range(len(s)):
            t_matrix[i][i] = True
        # Only need to handle the bottom-left triangle of the matrix.
        for i in range(1, len(s)):
            for j in range(i):
                if s[i] == s[j]:
                    if i - j < 3:  # e.g., 'a', 'aba'
                        t_matrix[j][i] = True
                    else:
                        t_matrix[j][i] = t_matrix[j + 1][i - 1]
                if t_matrix[j][i] and (i - j + 1) > max_len:
                    max_len = i - j + 1
                    max_substring = s[j:i + 1]

        return max_substring
