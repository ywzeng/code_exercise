# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_func(self, head: ListNode, node_num: int, k: int) -> ListNode:
        """ If the node num less than k, leave it as is. """
        if node_num < k:
            return head, None
        prior_node, next_node = None, None
        current_node = head
        for i in range(node_num):
            next_node = current_node.next
            current_node.next = prior_node
            prior_node = current_node
            current_node = next_node
        return prior_node, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        
        # Traverse the linked list.
        node_num = 0
        current = head
        while current:
            node_num += 1
            current = current.next
        
        if node_num < k:
            return head

        head_list = []
        # Divide the linked list into node_num/k (round up) parts.
        current_node = head
        i = 0
        while i < node_num:
            head_list += [current_node]
            sub_node_num = k if (i+k <= node_num) else (node_num-i)
            for j in range(i, i+sub_node_num):
                current_node = current_node.next
            i += k
        # Reverse the sub linked lists, respectively.
        last_tail_node = None
        for i, head_node in enumerate(head_list):
            sub_node_num = k if ((i+1)*k <= node_num) else (node_num-i*k)
            sub_head_node, sub_tail_node = self.reverse_func(head_node, sub_node_num, k)
            # Connect the sub linked lists.
            if last_tail_node:
                last_tail_node.next = sub_head_node
            last_tail_node = sub_tail_node
            head_list[i] = sub_head_node

        return head_list[0]
