# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        fake_head = ListNode(0)
        fake_head.next = head

        current_node = head     # The cursor.
        current_prior_node = fake_head       # The node prior to the cursor.

        # Find the anchor node.
        while current_node and current_node.val < x:
            current_prior_node = current_node
            current_node = current_node.next
        # All the nodes are properly ordered.
        if not current_node:
            return head
        
        anchor_node = current_node      # Record the first node whose value greater or equal to 'x'.
        anchor_prior_node = current_prior_node        # The node prior to the anchor node.
        current_prior_node = current_node
        current_node = current_node.next
        while current_node:
            if current_node.val < x:
                current_prior_node.next = current_node.next
                anchor_prior_node.next = current_node
                current_node.next = anchor_node
                anchor_prior_node = current_node
                current_node = current_prior_node.next
            else:
                current_prior_node = current_node
                current_node = current_node.next
        return fake_head.next
