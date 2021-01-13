# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0206.py
@time: 2021/1/13
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return

        prior_node, next_node = None, None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = prior_node
            prior_node = current_node
            current_node = next_node
        return prior_node
