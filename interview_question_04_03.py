# -*- coding: utf-8 -*-

"""
@author: zyw
@file: interview_question_04_03.py
@time: 2021/1/12
"""

"""
Question Source: https://leetcode-cn.com/problems/list-of-depth-lcci/
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists). 
Return a array containing all the linked lists.

Example:
Input: [1,2,3,4,5,null,7,8]

        1
       /  \ 
      2    3
     / \    \ 
    4   5    7
   /
  8

Output: [[1],[2,3],[4,5,7],[8]]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        """
        Push all the child nodes of all nodes in one layer into the stack in each time.
        Pop all the nodes from the stack in each time.
        All the nodes poped from the stack will be aggregated into one LinkedList.
        """
        if not tree:
            return []

        result_list = []  # Store the linkedList.
        stack = [tree]

        while stack:
            prior_node = None
            for i, node in enumerate(stack):
                if i == 0:
                    prior_node = ListNode(stack[0].val)
                    result_list += [prior_node]
                else:
                    current_node = ListNode(stack[i].val)
                    prior_node.next = current_node
                    prior_node = current_node

            temp_list = []
            for node in stack:
                if node.left:
                    temp_list += [node.left]
                if node.right:
                    temp_list += [node.right]
            stack = temp_list
        return result_list
