# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        fake_head = ListNode(-1, head)
        prior = fake_head
        cur = head
        while cur:
            if cur.val == val:
                prior.next = cur.next
            else:
                prior = cur
            cur = cur.next
        return fake_head.next
