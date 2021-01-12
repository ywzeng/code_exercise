# -*- coding: utf-8 -*-

"""
@author: zyw
@file: sword_to_offer_54.py
@time: 2021/1/12
"""

"""
Given a BST, get the k-th biggest node.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
        In a BST, the biggest node is the rightmost node, and the smallest node is the leftmost node.
        The root node is bigger than the nodes in its left sub-tree.
        The root node is smaller than the nodes in its right sub-tree.
        In this question, we need to back traverse the tree from right to left.
        In deed, it is a Inorder Traverse problem. We just need to modify the order 'left-middle-right' to 'right-middle-left'.
        """
        if not root:
            return

        temp_index = 0
        stack = []
        current_node = root
        while stack or current_node:
            if current_node:
                stack += [current_node]
                current_node = current_node.right
            else:
                current_node = stack.pop()
                temp_index += 1
                if temp_index == k:
                    return current_node.val
                current_node = current_node.left
