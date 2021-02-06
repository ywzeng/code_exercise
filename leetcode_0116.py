"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution_Recursion:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        # Recursively process the left and right sub-tree.
        self.connect(root.left)
        self.connect(root.right)
        return root

    
class Solution_Layer_Traverse:
    def connect(self, root: 'Node') -> 'Node':
        """ Layer Traverse. """
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
                    queue += [temp_queue[i].right]
            temp_queue[-1].next = None
            if temp_queue[-1].left:
                queue += [temp_queue[-1].left]
                queue += [temp_queue[-1].right]
        return root
