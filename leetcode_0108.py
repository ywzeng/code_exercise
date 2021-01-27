# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build_tree(nums: list, left: int, right: int, root_node: TreeNode) -> None:
            if left > right:
                return
            mid = (left + right) // 2
            root_node.val = nums[mid]
            if left < mid:
                left_node = TreeNode(0)
                root_node.left = left_node
                build_tree(nums, left, mid-1, left_node)
            if mid < right:
                right_node = TreeNode(0)
                root_node.right = right_node
                build_tree(nums, mid+1, right, right_node)
        
        if not nums:
            return
        root_node = TreeNode(0)
        build_tree(nums, 0, len(nums)-1, root_node)
        return root_node
