# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current_node = head
        while current_node:
            if current_node.next and current_node.next.val == current_node.val:
                temp_next_node = current_node.next
                current_node.next = current_node.next.next
                temp_next_node.next = None
            else:
                current_node = current_node.next
        return head
