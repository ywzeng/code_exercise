# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        1. Fast-slow pointers to find the mid index;
        2. Reverse the nodes from mid to the tail;
        3. Compare the node's value between [0: mid], [mid+1:].
        """
        if not head:
            return True
        slow, quick = head, head
        while quick.next and quick.next.next:
            # if quick.next -> even; if quick.next.next -> odd.
            slow = slow.next
            quick = quick.next.next
        
        # Reverse the [mid+1:]
        temp_head = slow.next
        prior_node = None
        while temp_head:
            next_node = temp_head.next
            temp_head.next = prior_node
            prior_node = temp_head
            temp_head = next_node
        slow.next = None        # Break the connection between the two sub linked lists.
        tail = prior_node
        while tail:
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next
        return True
