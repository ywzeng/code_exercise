# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_Recursion:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check_two_tree(root_1: TreeNode, root_2: TreeNode) -> bool:
            # Both the two trees are None -> symmetric.
            if not root_1 and not root_2:
                return True
            # Only one tree is None, while the other is not None -> unsymmetric.
            elif not root_1 or not root_2:
                return False
            # Both the two trees are not None, further check the values of the their root node and the symmetry of their sub-trees.
            # The two trees are symmetric means that the left sub-tree of tree_1 is equal to the right sub-tree of tree_2, vice versa.
            else:
                return root_1.val == root_2.val and check_two_tree(root_1.left, root_2.right) and check_two_tree(root_1.right, root_2.left)
        return check_two_tree(root, root)


class Solution_Iteration:
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
