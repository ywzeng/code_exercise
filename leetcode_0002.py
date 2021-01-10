# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0002.py
@time: 2021/1/10
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Create the calculate result node dynamically.
        Namely, if there is no calculate result, do not create result node.
        """
        result_node = ListNode()
        result_start_node = result_node
        carry_num = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            temp_sum = x + y + carry_num
            result_node_num = temp_sum % 10
            carry_num = temp_sum // 10
            new_node = ListNode(result_node_num)
            result_node.next = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            result_node = result_node.next
        if carry_num:
            new_node = ListNode(carry_num)
            result_node.next = new_node
        return result_start_node.next
