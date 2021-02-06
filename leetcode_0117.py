"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
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
