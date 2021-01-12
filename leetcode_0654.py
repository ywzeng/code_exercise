# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0654.py
@time: 2021/1/12
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: list) -> TreeNode:
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])

        big_index = nums.index(max(nums))
        root_node = TreeNode(nums[big_index])
        left_node = self.constructMaximumBinaryTree(nums[:big_index])
        right_node = self.constructMaximumBinaryTree(nums[big_index + 1:])
        root_node.left = left_node
        root_node.right = right_node
        return root_node
