class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MinStack_Slow:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.head = LinkedNode(float('-inf'))       # Always point to the node with the smallest value.

    def push(self, x: int) -> None:
        self.stack += [x]
        cur_node = self.head.next
        prior_node = self.head
        while cur_node and cur_node.val < x:
            prior_node = cur_node
            cur_node = cur_node.next
        new_node = LinkedNode(x)
        if cur_node:
            new_node.next = cur_node
        prior_node.next = new_node

    def pop(self) -> None:
        if not self.stack:
            return
        poped_num = self.stack.pop()
        cur_node = self.head.next
        prior_node = self.head
        while cur_node.val != poped_num:
            prior_node = cur_node
            cur_node = cur_node.next
        prior_node.next = cur_node.next
        del cur_node

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.head.next.val if self.stack else None
