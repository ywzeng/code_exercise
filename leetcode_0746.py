# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0746.py
@time: 2021/1/13
"""


class Solution:
    def minCostClimbingStairs(self, cost: list) -> int:
        """
        DP
        dp[0] = cost[0]
        dp[1] = min(dp[0]+cost[1], cost[1])     # One step or two step.
        dp[2] = min(dp[1]+cost[2], dp[0]+cost[2])
        ...
        dp[n] = min(dp[n-1]+cost[n], dp[n-2]+cost[n])
        Note that, the last step is to get to the top of the building, which has no cost.
        Thus, final_cost = min(dp[n], dp[n-1]).
        """
        dp = [0 for i in range(len(cost))]

        dp[0] = cost[0]
        dp[1] = min(dp[0] + cost[1], cost[1])
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        return min(dp[-1], dp[-2])
