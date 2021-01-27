# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result_list = []
        flag = True
        queue = [root]
        while queue:
            temp_list = queue[:]
            val_list = []
            queue = []
            for node in temp_list:
                if node.left:
                    queue += [node.left]
                if node.right:
                    queue += [node.right]
                val_list += [node.val]
            # Reverse or not is based on the flag.
            result_list += [val_list[:]] if flag else [val_list[::-1]]
            flag = not flag
        return result_list
