# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build_BST(self, left: int, right: int) -> TreeNode:
        result_list = []
        if left > right:
            result_list += [None]
            return result_list
        for i in range(left, right+1):
            # list format
            left_sub_nodes = self.build_BST(left, i-1)
            right_sub_nodes = self.build_BST(i+1, right)
            # Already got the nodes of left and right sub-trees. Combine all the candidates.
            # That is, taking 'i' as the root node, enumerate how many conbinations are there for the left and right sub-trees, respectively.
            # Actually, there are len(left_sub_nodes)*len(right_sub_nodes) combinations when the root is 'i'.
            for left_node in left_sub_nodes:
                for right_node in right_sub_nodes:
                    temp_root = TreeNode(i)
                    temp_root.left = left_node
                    temp_root.right = right_node
                    result_list += [temp_root]
        return result_list
        
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.build_BST(1, n)
