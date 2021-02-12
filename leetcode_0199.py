# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """ Level Traverse. """
        if not root:
            return []
        result_list = []
        queue = [root]
        while queue:
            result_list += [queue[0].val]
            temp_queue = queue[:]
            queue = []
            for node in temp_queue:
                if node.right:
                    queue += [node.right]
                if node.left:
                    queue += [node.left]
        return result_list
