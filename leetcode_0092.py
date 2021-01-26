# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        fake_root = ListNode(0)
        fake_root.next = head
        left_node, right_node = fake_root, None      # Record the nodes just before m and after n.
        current_node = head
        left_index, right_index = 0, m
        # Find the left node.
        while left_index < m-1:
            left_node = current_node
            current_node = current_node.next
            left_index += 1
        # Reverse the sub linked list in [m, n]
        prior_node = None
        temp_sub_list_head = current_node
        while right_index <= n:
            right_index += 1
            right_node = current_node.next
            # Reverse
            next_node = current_node.next
            current_node.next = prior_node
            prior_node = current_node
            current_node = next_node
        # Connect the left and right nodes with the reverse sub linked list.
        if left_node:
            left_node.next = prior_node
        if right_node:
            temp_sub_list_head.next = right_node
        return fake_root.next
