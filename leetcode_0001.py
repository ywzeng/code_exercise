# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0001.py
@time: 2021/1/10
"""


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        """
        even = odd + odd
        even = even + even
        odd = even + odd
        """
        is_odd = False
        if target % 2 == 1:
            is_odd = True
        has_minus = False
        for num in nums:
            if num < 0:
                has_minus = True
                break

        if is_odd:      # target is odd
            find_even = False
            for i in range(len(nums) - 1):
                if not has_minus and nums[i] > target:
                    continue
                if nums[i] % 2 == 1:
                    # i is odd
                    find_even = True
                for j in range(i+1, len(nums)):
                    if not has_minus and nums[j] > target:
                        continue
                    if find_even:       # i is odd, find even
                        if nums[j] % 2 == 0 and nums[i]+nums[j] == target:
                            return [i, j]
                    else:       # i is even, find odd
                        if nums[j] % 2 == 1 and nums[i] + nums[j] == target:
                            return [i, j]
        else:       # target is even
            for i in range(len(nums) - 1):
                find_even = False
                if not has_minus and nums[i] > target:
                    continue
                if nums[i] % 2 == 0:
                    # i is even
                    find_even = True
                for j in range(i+1, len(nums)):
                    if not has_minus and nums[j] > target:
                        continue
                    if find_even:       # i is even, find even
                        if nums[j] % 2 == 0 and nums[i] + nums[j] == target:
                            return [i, j]
                    else:       # i is odd, find odd
                        if nums[j] % 2 == 1 and nums[i] + nums[j] == target:
                            return [i, j]