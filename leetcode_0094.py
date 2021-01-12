# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0094.py
@time: 2021/1/12
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return

        result_list = []
        stack = []
        current_node = root
        while stack or current_node:
            if current_node:
                stack += [current_node]
                current_node = current_node.left
            else:
                current_node = stack.pop()
                result_list += [current_node.val]
                current_node = current_node.right
        return result_list
