# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Double pointers.
        1. Check whether the it has a circle.
        2. Get the position of the entrance of the circle.
        """
        slow, fast = head, head
        temp_p = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                temp_p = head
                while temp_p != slow:
                    temp_p = temp_p.next
                    slow = slow.next
                break
        return temp_p
