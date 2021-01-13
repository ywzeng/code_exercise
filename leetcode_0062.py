# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0062.py
@time: 2021/1/13
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        All the elements in the first row or the first column are all 1.
        Because the robot can only turn right or down.
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        """
        if m == 1 or n == 1:
            return 1
        t_matrix = [[0 for i in range(n)] for j in range(m)]

        # Let values in the first row (or column) are all 1.
        for i in range(n):
            t_matrix[0][i] = 1
        for i in range(m):
            t_matrix[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                t_matrix[i][j] = t_matrix[i - 1][j] + t_matrix[i][j - 1]

        return t_matrix[m - 1][n - 1]
