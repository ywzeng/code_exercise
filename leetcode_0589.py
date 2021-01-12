# -*- coding: utf-8 -*-

"""
@author: zyw
@file: leetcode_0589.py
@time: 2021/1/12
"""

"""
Given an n-ary tree, return the preorder traversal of its nodes' values.
Do not use recursion method.
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> list:
        if not root:
            return []

        result_list = []
        stack = [root]
        while stack:
            current_node = stack.pop()
            result_list += [current_node.val]
            for child in current_node.children[::-1]:
                stack += [child]
        return result_list
