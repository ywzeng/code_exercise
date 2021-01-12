# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0222.py
@time: 2021/1/12
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_height(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def countNodes(self, root: TreeNode) -> int:
        """ 
        The count of nodes of a full binary tree is (2^n-1).
        """
        if not root:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if left_height == right_height:     # The left sub-tree is a complete binary tree.
            # 1 + 2^(left_height) - 1 + (right nodes)
            # pow(2, n) == (1 << n)
            return (1 << left_height) + self.countNodes(root.right)
        else:       # The right sub-tree is a complete binary tree.
            # 1 + (left nodes) + 2^(right_height) - 1
            return self.countNodes(root.left) + (1 << right_height)
