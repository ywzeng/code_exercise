"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution_O1_Space:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = self.get_next(root.next)
        if root.right:
            root.right.next = self.get_next(root.next)
        # Recursively parse the left and right sub-tree.
        # Parse the right sub-tree first.
        # Because connecting the next of root.left need to iteratively get the sub-nodes of root.next.
        self.connect(root.right)
        self.connect(root.left)
        return root
    
    def get_next(self, root: 'None') -> 'Node':
        while root:
            if root.left:
                return root.left
            if root.right:
                return root.right
            root = root.next
        return None


class Solution_Queue:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = [root]
        while queue:
            temp_queue = queue[:]
            queue = []
            for i in range(len(temp_queue)-1):
                temp_queue[i].next = temp_queue[i+1]
                if temp_queue[i].left:
                    queue += [temp_queue[i].left]
                if temp_queue[i].right:
                    queue += [temp_queue[i].right]
            if temp_queue[-1].left:
                queue += [temp_queue[-1].left]
            if temp_queue[-1].right:
                queue += [temp_queue[-1].right]
        return root
