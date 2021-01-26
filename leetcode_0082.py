# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        prior_node, left = None, head
        while left.next:
            right = left.next
            if right.val != left.val:
                prior_node = left
                left = right
            else:
                while left.val == right.val:
                    if right.next:
                        right = right.next
                    else:
                        if prior_node:
                            prior_node.next = None
                            return head
                        else:
                            head = None
                            return head
                # Skip the redudant nodes.
                if prior_node:
                    prior_node.next = right
                else:
                    head = right
                left = right
        return head         
