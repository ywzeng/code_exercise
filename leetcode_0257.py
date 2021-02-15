# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_Recursion:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        path_list = []
        # Get all the paths within its left sub-tree.
        for sub_path in self.binaryTreePaths(root.left):
            temp_path = str(root.val) + '->' + sub_path
            path_list += [temp_path]
        # Get all the paths within its right sub-tree.
        for sub_path in self.binaryTreePaths(root.right):
            temp_path = str(root.val) + '->' + sub_path
            path_list += [temp_path]
        return path_list
