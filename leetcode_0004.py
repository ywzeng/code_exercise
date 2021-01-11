# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0004.py
@time: 2021/1/11
"""

"""
    Socution_1 is thought by myself. I use the Seclect Sort Algorithm to get the top-(N/2) values.
    Then calculate the middle value, namely the last value of top-(N/2).
    But the time complexity is O(n^2). But the time complexity required by the question is O(log(m+n)).
"""


class Solution_1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Only need to find the top-(N/2) or Top-(N/2+1) nums, depeending on the parity of the (nums1+nums2).
        Here we use the Select Sort Algorithm to get the top-k numbers.
        """
        if not nums1 and not nums2:
            return
        elif not nums1 and len(nums2) == 1:
            return nums2[0] / 1
        elif len(nums1) == 1 and not nums2:
            return nums1[0] / 1

        nums = nums1 + nums2
        len_total = len(nums)

        range_times = len_total // 2 if len_total <= 2 else len_total // 2 + 1

        # Use Select Sort Algorithm to get the Top-K numbers.
        for i in range(range_times):
            # Get the max value of the [i:]
            max_index = i + 1
            for j in range(i + 1, len_total):
                if nums[j] > nums[max_index]:
                    max_index = j
            if nums[max_index] > nums[i]:
                nums[i], nums[max_index] = nums[max_index], nums[i]

        if len_total % 2 == 0:
            middle_value = (nums[len_total // 2] + nums[len_total // 2 - 1]) / 2
        else:
            middle_value = nums[len_total // 2]
        return middle_value
