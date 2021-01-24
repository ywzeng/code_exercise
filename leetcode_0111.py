# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """ Use level traverse to find the shallowest leaf node。 """
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            poped_node_list = queue[:]
            queue = []
            for poped_node in poped_node_list:
                if not poped_node.left and not poped_node.right:
                    return depth
                if poped_node.left:
                    queue += [poped_node.left]
                if poped_node.right:
                    queue += [poped_node.right]
