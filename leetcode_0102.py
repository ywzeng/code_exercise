# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result_list = []
        while queue:
            temp_queue = []
            while queue:
                temp_queue += [queue.pop(0)]
            temp_layer_result = []
            while temp_queue:
                current_node = temp_queue.pop(0)
                temp_layer_result += [current_node.val]
                if current_node.left:
                    queue += [current_node.left]
                if current_node.right:
                    queue += [current_node.right]
            result_list += [temp_layer_result]
        return result_list
