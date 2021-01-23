# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """ Level traverse. """
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            for i in range(len(queue)):
                if queue[i] and queue[len(queue)-1-i]:
                    if queue[i].val != queue[len(queue)-1-i].val:
                        return False
                elif (queue[i] and not queue[len(queue)-1-i]) or (not queue[i] and queue[len(queue)-1-i]):
                    return False
            temp_list = []
            while queue:
                poped_node = queue.pop(0)
                if poped_node:
                    temp_list += [poped_node.left]
                    temp_list += [poped_node.right]
            queue = temp_list[:]
        return True
