# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Use the quick-slow pointers. The quick pointer moves 'n' steps before the slow pointer moves.
        When the quick pointer moves to the end of the list, the index of the the slow pointer is the target N-th node from end of the list.
        """
        if not head:
            return
        if n == 1 and not head.next:
            return

        slow_p, quick_p, prior_node = head, head, None
        for i in range(n):
            quick_p = quick_p.next
        while quick_p:
            prior_node = slow_p
            slow_p = slow_p.next
            quick_p = quick_p.next
        if prior_node:
            prior_node.next = slow_p.next if slow_p.next else None
            slow_p.next = None
        else:       # The slow pointer has not moved, keeping pointing to the head .
            head = head.next
        return head
