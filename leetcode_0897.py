# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0897.py
@time: 2021/1/12
"""

"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

When solving this problem, we need to dynamically modify the node to be its prior node's right node, and empty its left node.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
        1. Inorder traverse the tree (left - middle - right);
        2. Build the right-child-only tree based on the above traverse result.
        Note that, do not use recursion method.
        """
        if not root:
            return

        # The root of the right-child-only tree.
        new_root = TreeNode(0)
        temp_node = new_root

        # 1. Inorder traverse the tree.
        stack = []
        current_node = root
        while stack or current_node:
            if current_node:
                stack += [current_node]
                current_node = current_node.left
            else:
                poped_node = stack.pop()
                current_node = poped_node.right
                # The left of the poped node has been parsed before, so we set its left to None.
                poped_node.left = None
                temp_node.right = poped_node
                temp_node = temp_node.right
        return new_root.right
