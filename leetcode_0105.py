# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Inorder traverse get the root node first, while preorder traverse get the left node first.
        Thus, we can first get the root node first from the preorder list, then get the left nodes and right nodes of that root from the preorder list.
        Then, back to the preprder list to find the root of the left and right sub-trees, respectively.
        We can use recursion method here.
        """
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])
        root_inorder_index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:1+root_inorder_index], inorder[:root_inorder_index])
        root.right = self.buildTree(preorder[1+root_inorder_index:], inorder[root_inorder_index+1:])
        return root
