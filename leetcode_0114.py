# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        prior_node = None
        stack = [root]
        while stack:
            current_node = stack.pop()
            if current_node.right:
                stack += [current_node.right]
            if current_node.left:
                stack += [current_node.left]
            current_node.left = None
            if prior_node:
                prior_node.right = current_node
            prior_node = current_node
        return root
