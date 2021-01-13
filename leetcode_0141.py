# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0141.py
@time: 2021/1/13
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """ Use quick && slow point to solve this problem. """
        if not head:
            return False
        slow_point = head
        quick_point = head.next
        has_ring = False
        while slow_point and quick_point:
            if slow_point == quick_point:
                has_ring = True
                break
            if not quick_point.next:
                break
            slow_point = slow_point.next
            quick_point = quick_point.next.next
        return has_ring
