# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_stupid:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return

        def merge2LinkedLists(l1: ListNode, l2: ListNode) -> ListNode:
            if not l1 and not l2:
                return 
            elif l1 and not l2:
                return l1
            elif not l1 and l2:
                return l2
            if l1.val <= l2.val:
                head = l1
                l1 = l1.next
            else:
                head = l2
                l2 = l2.next
            current_node = head
            while l1 and l2:
                if l1.val <= l2.val:
                    current_node.next = l1
                    l1 = l1.next
                else:
                    current_node.next = l2
                    l2 = l2.next
                current_node = current_node.next
            if l1:
                current_node.next = l1
            if l2:
                current_node.next = l2
            return head

        final = lists[0]
        
        for i in range(1, len(lists)):
            final = merge2LinkedLists(final, lists[i])
        return final
