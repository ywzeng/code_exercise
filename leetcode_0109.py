# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        Fast-slow pointers.
        Actually, it is another form of binary search.
        """
        if not head:
            return
        elif not head.next:
            return TreeNode(head.val)

        prior_node = head
        slow_pointer = head.next
        quick_pointer = slow_pointer.next
        # Get the middle node.
        while quick_pointer and quick_pointer.next:
            prior_node = slow_pointer
            slow_pointer = slow_pointer.next
            quick_pointer = quick_pointer.next.next
        
        # Recursively get the middle nodes.
        # The middle nodes of before and after slow pointer is the root nodes of the left and right sub-trees.
        prior_node.next = None      # Break the relation between slow_pointer and its prior nodes.
        root_node = TreeNode(slow_pointer.val)
        root_node.left = self.sortedListToBST(head)     # From the head to slow_pointer-1
        root_node.right = self.sortedListToBST(slow_pointer.next)       # From slow_pointer+1 to the tail.
        return root_node
