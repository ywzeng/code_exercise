# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        fake_root = ListNode()
        fake_root.next = head
        left = head
        prior = fake_root
        while left and left.next:
            right = left.next
            if right.val != left.val:
                prior, left = left, right
            else:
                while right and right.val == left.val:
                    right = right.next
                prior.next = right
                left = right
        return fake_root.next
