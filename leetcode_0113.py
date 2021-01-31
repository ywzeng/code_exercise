# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def back_track(current_node: TreeNode, track_list: list, result_list: list, track_sum: int, targetSum: int) -> None:
            # Leaf node.
            if not current_node.left and not current_node.right:
                if track_sum + current_node.val == targetSum:
                    temp_list = [temp_node.val for temp_node in track_list] + [current_node.val]
                    result_list += [temp_list]
                return
            # Relay node.
            else:
                track_sum += current_node.val
                track_list += [current_node]
                if current_node.left:
                    back_track(current_node.left, track_list, result_list, track_sum, targetSum)
                if current_node.right:
                    back_track(current_node.right, track_list, result_list, track_sum, targetSum)
                track_sum -= current_node.val
                track_list.pop()
        if not root:
            return []
        track_list, result_list = [], []
        back_track(root, track_list, result_list, 0, targetSum)
        return result_list
       
