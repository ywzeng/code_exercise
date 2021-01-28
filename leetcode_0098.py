# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Get the greatest node, l_greatest, in its left sub-tree, and the greatest node, r_smallest, in its right sub-tree.
        If l_greatest <= root <= r_smallest, it is a binary search tree.
        """
        def check_bst(root: TreeNode) -> list:
            """ The return value is a list of [bool, smallest, greatest]"""
            if not root:
                return True, None, None
            
            is_left_bst, l_smallest, l_greatest = check_bst(root.left)
            is_right_bst, r_smallest, r_greatest = check_bst(root.right)

            if not is_left_bst or not is_right_bst:
                return False, None, None
            else:
                if l_greatest and l_greatest >= root.val:
                    return False, None, None
                if r_smallest and r_smallest <= root.val:
                    return False, None, None
                l_smallest = l_smallest if l_smallest else root.val
                r_greatest = r_greatest if r_greatest else root.val
                return True, l_smallest, r_greatest
        return check_bst(root)[0]
