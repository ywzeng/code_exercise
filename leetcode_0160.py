# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return
        
        temp_A, temp_B = headA, headB
        while temp_A != temp_B:
            """
            If A and B have intersection point, the point is when temp_A == temp_B.
            If A and B have no intersection point, temp_A and temp_B will be None in the end.
            temp_A and temp_B will travel the same distance.
            """
            # A arrive at the tail of List A.
            temp_A = headB if not temp_A else temp_A.next
            # B arrive at the tail of List B.
            temp_B = headA if not temp_B else temp_B.next
        return temp_A
