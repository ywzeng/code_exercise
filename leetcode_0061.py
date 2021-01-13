# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0061.py
@time: 2021/1/13
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """ Use an additional list to store the replaced Node. """
        if not head:
            return
        if not head.next:
            return head

        current_node_list = []
        while head:
            current_node_list += [head]
            head = head.next
        node_num = len(current_node_list)

        k = k % node_num
        if k == 0:
            return current_node_list[0]

        temp_list = [None for i in range(node_num)]  # Additional list to store the replaced node.
        for i in range(node_num):
            target_index = i + k if i + k < node_num else i + k - node_num
            temp_list[target_index] = current_node_list[target_index]
            current_node_list[target_index] = temp_list[i] if temp_list[i] else current_node_list[i]

        for i in range(node_num - 1):
            current_node_list[i].next = current_node_list[i + 1]
        current_node_list[-1].next = None
        return current_node_list[0]

