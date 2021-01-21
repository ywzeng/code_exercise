# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """ 
        Postorder of the tree is the reverse of preorder.
        Preorder: root -> left -> right.
        Reverse preorder: right -> left -> root.
        Reverse the order of left and right in the reverse preorder: left -> right -> root.
        Postorder: left -> right -> root.
        """
        if not root:
            return []
        stack = [root]
        result_list = []
        while stack:
            current_node = stack.pop()
            result_list += [current_node.val]
            if current_node.left:
                stack += [current_node.left]
            if current_node.right:
                stack += [current_node.right]
        return result_list[::-1]
