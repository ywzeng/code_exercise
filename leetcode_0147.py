# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        fake_head = ListNode(float('-inf'))
        fake_head.next = head
        cur_node = head
        prior_node = fake_head
        while cur_node:
            if cur_node.val >= prior_node.val:
                prior_node = cur_node
                cur_node = cur_node.next
            else:
                inserted_point = fake_head.next
                inserted_prior_node = fake_head
                # Get the insert point.
                while inserted_point.val < cur_node.val:
                    inserted_prior_node = inserted_point
                    inserted_point = inserted_point.next
                prior_node.next = cur_node.next
                inserted_prior_node.next = cur_node
                cur_node.next = inserted_point
                cur_node = prior_node.next
        return fake_head.next
