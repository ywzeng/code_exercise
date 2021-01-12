# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0110.py
@time: 2021/1/12
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_height(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        if left_height >= 0 and right_height >= 0 and abs(left_height - right_height) <= 1:
            return max(left_height, right_height) + 1
        else:
            return -1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.get_height(root) >= 0
