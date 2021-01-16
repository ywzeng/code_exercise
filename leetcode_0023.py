# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_divide_conquer:
    def merge_2_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        if l1 and not l2:
            return l1
        if not l1 and l2:
            return l2

        if l1.val <= l2.val:
            root = l1
            l1 = l1.next
        else:
            root = l2
            l2 = l2.next
        current_node = root
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
        return root

    def divide_conquer_merge(self, lists: List[ListNode], left: int, right: int) -> ListNode:
        """ Recursively divide the list into two parts """
        if left == right:
            return lists[left]
        if left > right:
            return
        mid = (left + right) // 2
        return self.merge_2_lists(self.divide_conquer_merge(lists, left, mid), self.divide_conquer_merge(lists, mid+1, right))

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.divide_conquer_merge(lists, 0, len(lists)-1)


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
