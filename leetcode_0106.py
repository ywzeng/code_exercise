# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        In-order traverse: left-root-right.
        Post-order traverse: left-right-root.
        Post-order traverse is a special kind of reverse of pre-order traverse.
        We can reverse the post-order list to the pre-order list.
        E.g., [9,15,7,20,3] -> [3,20,7,15,9].
        The reverse order is root-right-left.
        So, we can first get the root node, and follow the problem #105 to solve this problem.
        """
        def specialReverseBuildTree(inorder: list, special_preorder: list) -> TreeNode:
            if not inorder or not special_preorder:
                return
            root = TreeNode(special_preorder[0])
            root_inorder_index = inorder.index(root.val)
            root.left = specialReverseBuildTree(inorder[:root_inorder_index], special_preorder[len(inorder)-root_inorder_index:])
            root.right = specialReverseBuildTree(inorder[root_inorder_index+1:], special_preorder[1: len(inorder)-root_inorder_index])
            return root

        special_preorder = [num for num in postorder[::-1]]
        return specialReverseBuildTree(inorder, special_preorder)
