# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def back_track(current_node: TreeNode, track_list: list, result_num: int) -> int:
            # Stop condition.
            if not current_node.left and not current_node.right:
                temp_num = 0
                for i, num in enumerate(track_list[::-1]):
                    temp_num += num * pow(10, i)
                result_num += temp_num
                return result_num
            
            if current_node.left:
                track_list += [current_node.left.val]
                result_num = back_track(current_node.left, track_list, result_num)
                track_list.pop()
            if current_node.right:
                track_list += [current_node.right.val]
                result_num = back_track(current_node.right, track_list, result_num)
                track_list.pop()
            return result_num
        
        if not root:
            return 0

        track_list = [root.val]
        result_num = 0
        result_num = back_track(root, track_list, result_num)
        return result_num
