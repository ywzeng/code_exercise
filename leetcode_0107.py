# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result_list = []
        queue = [root]
        while queue:
            poped_node_list = []
            while queue:
                poped_node_list += [queue.pop(0)]
            for i, poped_node in enumerate(poped_node_list):
                if poped_node.left:
                    queue += [poped_node.left]
                if poped_node.right:
                    queue += [poped_node.right]
                poped_node_list[i] = poped_node.val
            result_list += [poped_node_list]
        return result_list[::-1]   
