# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_check_sub_tree:
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
    

class Solution_middle_order_traverse:
    def isValidBST(self, root: TreeNode) -> bool:
        """ The middle order traverse of a BST is asscending. """
        def middle_traverse(root: TreeNode, result_list: list) -> None:
            if not root:
                return None
            
            middle_traverse(root.left, result_list)
            result_list += [root.val]
            middle_traverse(root.right, result_list)
        result_list = []
        middle_traverse(root, result_list)
        if len(result_list) < 2:
            return True
        for i in range(1, len(result_list)):
            if result_list[i] <= result_list[i-1]:
                return False
        return True
