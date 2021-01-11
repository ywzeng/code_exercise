# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0228.py
@time: 2021/1/11
"""


class Solution:
    def summaryRanges(self, nums: list) -> list:
        if len(nums) == 1:
            return [str(nums[0])]
        return_list = []
        start_index  = 0
        while start_index < len(nums):
            end_index = start_index
            while end_index+1 < len(nums) and nums[end_index+1] - nums[end_index] == 1:
                end_index += 1
            if start_index != end_index:
                return_list += [str(nums[start_index]) + '->' + str(nums[end_index])]
            else:
                return_list += [str(nums[start_index])]
            start_index = end_index + 1
        return return_list
