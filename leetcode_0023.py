# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    We employ three methods to solve this problem.
    1. Priority Queue;
    2. Divide and Conquer;
    3. Brute Force Merge;
    In which, the Divide-Conquer method is the fastest, followed by the Priority-Queue method, and the Brute-Force-Merge method is the slowest method.
    Note that, We need to learn more about the Priority-Queue and the Heap-realted algorithms.
"""

from queue import PriorityQueue


# Define a priority queue item.
class PQueueItem:
    def __init__(self, node: ListNode, val: int):
        self.node = node
        self.val = val

    def __lt__(self, other_node):
        return self.val < other_node.val


class Solution_priority_queue:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        priority_queue = PriorityQueue()
        for head_node in lists:
            if head_node:
                priority_queue.put(PQueueItem(head_node, head_node.val))
        
        head = ListNode(0)      # Define a virtual head.
        prior_node = head
        while priority_queue.queue:
            current_pq_node = priority_queue.get()
            prior_node.next = current_pq_node.node
            prior_node = prior_node.next
            if current_pq_node.node.next:
                priority_queue.put(PQueueItem(current_pq_node.node.next, current_pq_node.node.next.val))
        return head.next


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
