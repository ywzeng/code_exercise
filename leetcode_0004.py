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
    
    The best solution of this question is to use Binary Search Algorithm.
    Use two divide lines to divide the two number list, making the numbers on the left of lines are all smaller than the numbers on the right of the lines.
    Dynamically move the divide lines, depending on the numbers beside the lines, that is the numbers one the left of lines must be smaller thatn the numbers on the right of the lines.
"""


class Solution_1:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        """
        Only need to find the top-(N/2) or Top-(N/2+1) nums, depeending on the parity of the (nums1+nums2).
        Here we use the Select Sort Algorithm to get the top-k numbers.
        """
        if not nums1 and len(nums2) == 1:
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


class Solution_2:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        """
        Use Binary Search Algorithm to dynamically search the list to find the median number.
        We should ensure that the numbers on the left side of median number are all smaller than the median number, and the numbers on the right side of median number are all bigger than the median number.
        Besides, the number of the numbers on the left is equal to the number of the numbers on the right.
        We use Binary Search Algorithm to dynamicaly reduce the search space -> O(log(m+n)) where m and n are the size of the input lists.
        If the number of the numbers is an even, the median value is equal to the average of sum of the two middle numbers.
        If the number of the numbers is an odd, the median value is the middle number.
        """
        nums1_len, nums2_len = len(nums1), len(nums2)
        k_1 = (nums1_len + nums2_len + 1) // 2  # the divide cursor of nums1
        k_2 = (nums1_len + nums2_len + 2) // 2  # the divide cursor of nums2
        return (self.get_k(nums1, 0, nums1_len - 1, nums2, 0, nums2_len - 1, k_1) +
                self.get_k(nums1, 0, nums1_len - 1, nums2, 0, nums2_len - 1, k_2)) / 2  # Recursion method to get the median number

    def get_k(self, nums1, start_1, end_1, nums2, start_2, end_2, k):
        """
        Search the K-th smallest number in the combination of nums1 and nums2.
        Dynamically modify the boundary of the two num lists (binary search).
        """
        nums1_len = end_1 - start_1 + 1
        nums2_len = end_2 - start_2 + 1
        # Make sure the nums1 are always shorter than nums2.
        if nums1_len > nums2_len:
            return self.get_k(nums2, start_2, end_2, nums1, start_1, end_1, k)
        # If the first list has no elements, the K-th number must be the k-th number in the second list.
        if nums1_len == 0:
            return nums2[start_2 + k - 1]  # The index of the element is start with 0, so we need to minus one.

        # If k == 1, indicating that we have found the k-th value, namely the median value.
        if k == 1:
            return min(nums1[start_1], nums2[start_2])

        # Get the index of the first number on the left side of the binary-partition point, i and j, namely (k/2 - 1).
        # If the binary-partition point is out of the lists (auctually, exceeds the element number of the list), directly use the rightmost index of the list as the binary-partition point.
        i = start_1 + min(nums1_len, k // 2) - 1
        j = start_2 + min(nums2_len, k // 2) - 1

        # nums[i] > nums2[j] means that all the numbers on the left side of nums[j] (including nums[j] itself) are all smaller than the median value, we can filter them and search the remaining elements to find the median value. The number of the filter elements is (k/2)-1.
        if nums1[i] > nums2[j]:
            return self.get_k(nums1, start_1, end_1, nums2, j + 1, end_2, k - (
                        j - start_2 + 1))  # Filter the 'must-be-smaller' elements to tighten the search space.
        else:
            return self.get_k(nums1, i + 1, end_1, nums2, start_2, end_2, k - (i - start_1 + 1))
