# -*- coding: utf-8 -*-

"""
@author: zyw
@file: tree_exercise.py
@time: 2021/1/7
"""


class Node(object):
    def __init__(self, data, l_child=None, r_child=None):
        self.data = data
        self.times = 0      # for the postorder traverse func.
        self.l_child = l_child
        self.r_child = r_child


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def add_node(self, data):
        temp_node = Node(data)
        if self.root is None:
            self.root = temp_node
            return
        queue = [self.root]
        while queue:
            curent_node = queue.pop(0)
            if curent_node.l_child is None:
                curent_node.l_child = temp_node
                return
            elif curent_node.r_child is None:
                curent_node.r_child = temp_node
                return
            else:
                queue += [curent_node.l_child]
                queue += [curent_node.r_child]

    def preorder_recursion(self, root):
        if root is None:
            return
        print(root.data)
        self.preorder_recursion(root.l_child)
        self.preorder_recursion(root.r_child)

    def inorder_recursion(self, root):
        if root is None:
            return
        self.inorder_recursion(root.l_child)
        print(root.data)
        self.inorder_recursion(root.r_child)

    def postorder_recursion(self, root):
        if root is None:
            return
        self.postorder_recursion(root.l_child)
        self.postorder_recursion(root.r_child)
        print(root.data)

    def preorder_non_recursion(self):
        """
        middle - left - right
        """
        if self.root is None:
            return
        stack = [self.root]
        while stack:
            current_node = stack.pop()
            print(current_node.data)
            if current_node.r_child:
                stack += [current_node.r_child]
            if current_node.l_child:
                stack += [current_node.l_child]

    def inorder_non_recursion(self):
        """left - middle - right"""
        if self.root is None:
            return
        stack = []
        current_node = self.root
        while stack or current_node:
            if current_node:
                stack += [current_node]
                current_node = current_node.l_child
            else:
                current_node = stack.pop()
                print(current_node.data)
                current_node = current_node.r_child

    def postorder_non_recursion_method_1(self):
        """
        left - right - middle
        One node should be parsed twice in this func.
        The first time is after the traverse of its left sub-tree.
        The second time is after traverse of its right sub-tree, and then output its own data.
        Therefore, we need a variable to indicate whether current node has been been visited.
        """
        if self.root is None:
            return
        stack = []
        current_node = self.root
        while stack or current_node:
            if current_node:
                stack += [current_node]
                current_node = current_node.l_child
            else:
                current_node = stack.pop()
                current_node.times += 1
                # Pop the first time is the sign of finishing the traverse of its left sub-tree.
                if current_node.times == 1:
                    stack += [current_node]
                    current_node = current_node.r_child
                # Pop the second time is the sign of finishing the traverse of its right sub-tree.
                elif current_node.times == 2:
                    print(current_node.data)
                    current_node = None     # An important step to back to its parent node.

    def postorder_non_recursion_method_2(self):
        """
        left - right - middle
        postorder traverse of one tree is equal to the reverse of preorder traverse of that tree.
        But in this preorder traverse, we need to reverse the traverse order of left and right sub-tree.
        Namely, middle -> right -> left, and finally reverse output the traverse result.
        :return:
        """
        if self.root is None:
            return
        stack = [self.root]
        output_list = []
        while stack:
            current_node = stack.pop()
            output_list += [current_node.data]
            if current_node.l_child:
                stack += [current_node.l_child]
            if current_node.r_child:
                stack += [current_node.r_child]
        print(output_list[::-1])

    def postorder_non_recursion_method_3(self):
        if self.root is None:
            return
        prior_visited_node = None
        current_node = None
        stack = [self.root]
        while stack:
            current_node = stack[-1]
            if (current_node.l_child is None and current_node.r_child is None) or (prior_visited_node and (prior_visited_node == current_node.l_child or prior_visited_node == current_node.r_child)):
                prior_visited_node = stack.pop()
                print(prior_visited_node.data)
            else:
                if current_node.r_child is not None:
                    stack += [current_node.r_child]
                if current_node.l_child is not None:
                    stack += [current_node.l_child]

    def breadth_traverse(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            print(current_node.data)
            if current_node.l_child:
                queue += [current_node.l_child]
            if current_node.r_child:
                queue += [current_node.r_child]


class BST(object):
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        """
        Insert the bigger one into the left sub-tree, and insert the smaller one into the right sub-tree.
        """
        target_node = Node(data)
        if self.root is None:
            self.root = target_node
            return

        # If the data is already in the tree, return.
        if self.search_node_non_recursion(self.root, data) is not None:
            return

        current_node = self.root
        temp_parent_node = None     # The parent of current node.
        while current_node:
            # current node is None indicates that its parent node is the parent node of the inserted one.
            temp_parent_node = current_node
            if data < current_node.data:
                current_node = current_node.l_child
            else:
                current_node = current_node.r_child
        if data > temp_parent_node.data:
            temp_parent_node.r_child = target_node
        else:
            temp_parent_node.l_child = target_node

    def create_bst(self, data_list):
        for data in data_list:
            self.insert_node(data)

    def search_min(self, root_node):
        """ The leftmost node has the minimum value """
        if root_node is None:
            return
        min_node = None
        stack = [root_node]
        while stack:
            current_node = stack.pop()
            if current_node.l_child is not None:
                stack += [current_node.l_child]
            else:
                min_node = current_node
                break
        return min_node

    def search_max(self, root_node):
        """ The rightmost node has the maximum value """
        if root_node is None:
            return
        max_node = None
        stack = [root_node]
        while stack:
            current_node = stack.pop()
            if current_node.r_child is not None:
                stack += [current_node.r_child]
            else:
                max_node = current_node
                break
        return max_node

    def search_node_recursion(self, root_node, data):
        """ Return the node with its value equal to the given data """
        if root_node is None:
            return
        if data < root_node.data:       # Search the left sub-tree
            return self.search_node_recursion(root_node.l_child, data)
        elif data > root_node.data:     # Search the right sub-tree
            return self.search_node_recursion(root_node.r_child, data)
        else:       # Get the matched node.
            return root_node

    def search_node_non_recursion(self, root_node, data):
        if root_node is None:
            return
        match_node = None
        current_node = root_node
        while current_node:
            if current_node.data == data:
                match_node = current_node
                break
            # r_child or l_child is None means that this BST has no such node, and break the loop.
            if data > current_node.data:
                current_node = current_node.r_child
            else:
                current_node = current_node.l_child
        return match_node

    def remove_node(self, data):
        """
        Very important!!
        Three cases:
            1. If the target node is a leaf node, directly remove it.
            2. If the target node has only one child node, replace it with its child node;
            3. If the target node has two child nodes, replace it with the smallest node in its right sub-tree.
        :return:
        """
        if not self.root:
            return
        parent_node = None       # The parent of current node.
        current_node = self.root

        # Find the target node and its parent node.
        while current_node:
            if current_node.data == data:
                break
            parent_node = current_node
            if data > current_node.data:
                current_node = current_node.r_child
            else:
                current_node = current_node.l_child

        # Case 1: target node is a leaf node.
        if not current_node.l_child and not current_node.r_child:
            # The tree has only one node, and this node is the target node.
            if not parent_node:
                self.root = None
            else:
                if current_node.data < parent_node.data:
                    parent_node.l_child = None
                else:
                    parent_node.r_child = None
        # Case 2-1: target node has only a left child.
        elif current_node.l_child and not current_node.r_child:
            if current_node.data < parent_node.data:
                parent_node.l_child = current_node.l_child
            else:
                parent_node.r_child = current_node.l_child
            del current_node
        # Case 2-2: target node has only a right child.
        elif not current_node.l_child and current_node.r_child:
            if current_node.data < parent_node.data:
                parent_node.l_child = current_node.r_child
            else:
                parent_node.r_child = current_node.r_child
            del current_node
        # Case 3: target node has both the left child and the right child. Find the smallest node in its right sub-tree.
        # The smallest node of one BST tree is either the leftmost node or the root node.
        else:
            right_root_node = current_node.r_child      # root node of the right sub-tree
            # 3-1: The smallest node is the root node.
            if not right_root_node.l_child:
                right_root_node.l_child = current_node.l_child
                if current_node.data < parent_node.data:
                    parent_node.l_child = right_root_node
                else:
                    parent_node.r_child = right_root_node
            # 3-2: The smallest node is the leftmost node.
            else:
                parent_node_of_leftmost = None      # The parent node of the leftmost node.
                leftmost_node = right_root_node
                # Find the leftmost node.
                while leftmost_node.l_child:
                    parent_node_of_leftmost = leftmost_node
                    leftmost_node = leftmost_node.l_child
                # Link the leftmost node to its new parent node.
                if current_node.data < parent_node.data:
                    parent_node.l_child = leftmost_node
                else:
                    parent_node.r_child = leftmost_node
                # Link the root of the left sub-tree of the removed node to the leftmost node
                leftmost_node.l_child = current_node.l_child
                # Link the root
                leftmost_node.r_child = right_root_node
                parent_node_of_leftmost.l_child = None
            del current_node

    def preorder_traverse(self):
        if not self.root:
            return
        stack = [self.root]
        while stack:
            current_node = stack.pop()
            print(current_node.data)
            if current_node.r_child:
                stack += [current_node.r_child]
            if current_node.l_child:
                stack += [current_node.l_child]


if __name__ == '__main__':
    a = [17,12,19,10,15,18,25,8,11,13,16,22,27,28,26]
    bst = BST()
    bst.create_bst(a)
    bst.remove_node(25)
    bst.preorder_traverse()
