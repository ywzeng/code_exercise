# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result_list = []
        while stack:
            current_node = stack.pop()
            result_list += [current_node.val]
            if current_node.right:
                stack += [current_node.right]
            if current_node.left:
                stack += [current_node.left]
        return result_list
