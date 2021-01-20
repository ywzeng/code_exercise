# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        
        stack1, stack2 = [p], [q]
        while stack1 and stack2:
            current_node_1 = stack1.pop()
            current_node_2 = stack2.pop()
            if current_node_1.val != current_node_2.val:
                return False
            # Right sub-tree.
            if current_node_1.right and current_node_2.right:
                stack1 += [current_node_1.right]
                stack2 += [current_node_2.right]
            elif (not current_node_1.right and current_node_2.right) or (current_node_1.right and not current_node_2.right):
                return False
            # Left sub-tree.
            if current_node_1.left and current_node_2.left:
                stack1 += [current_node_1.left]
                stack2 += [current_node_2.left]
            elif (not current_node_1.left and current_node_2.left) or (current_node_1.left and not current_node_2.left):
                return False
        return True
