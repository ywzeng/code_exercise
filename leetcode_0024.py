#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        
        current_node = head
        prior_node = head
        head = current_node.next
        while current_node and current_node.next:
            temp_next = current_node.next.next      # record the (i+2)-th node.
            prior_node.next = current_node.next
            current_node.next.next = current_node
            current_node.next = temp_next
            prior_node = current_node       # update the prior_node.
            current_node = temp_next        # update the current_node to the (i+1)-th node.
        return head

