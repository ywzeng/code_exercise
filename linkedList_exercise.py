# -*- coding: utf-8 -*-

"""
@author: zyw
@file: linkedList_exercise.py
@time: 2021/1/7
"""


class SingleLinkedNode(object):
    """
    The node of single linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    """
    Single linked list.
    """
    def __init__(self):
        self.__head = None       # One underline indicates private. Two underlines indicate absolutely private.

    def is_empty(self):
        return self.__head is None

    def get_length(self):
        current_node = self.__head
        length = 0
        while current_node is not None:
            current_node = current_node.next
            length += 1
        return length

    def traverse(self):
        current_node = self.__head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def add(self, data):
        """
        Add data to the head of the linked list.
        :return:
        """
        temp_node = SingleLinkedNode(data)
        temp_node.next = self.__head
        self.__head = temp_node

    def append(self, data):
        """
        Append node to the tail of the linked list.
        :return:
        """
        temp_node = SingleLinkedNode(data)
        if self.is_empty():
            self.__head = temp_node
        else:
            current_node = self.__head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = temp_node

    def insert(self, index, data):
        """
        Add data to the specified index.
        :return:
        """
        if index <= 0:
            self.add(data)
        elif index > self.get_length()-1:
            self.append(data)
        else:
            temp_node = SingleLinkedNode(data)
            # This variable indicates the node before the specified index. Namely insert the node after current node.
            current_index = 0
            current_node = self.__head
            while current_index < index-1:
                current_index += 1
                current_node = current_node.next
            temp_node.next = current_node.next
            current_node.next = temp_node

    def remove(self, data):
        current_node = self.__head
        prior_node = None
        while current_node is not None:
            if current_node.data == data:
                # The target node is the head.
                if prior_node is None:
                    self.__head = current_node.next
                else:
                    prior_node.next = current_node.next
                break
            prior_node = current_node
            current_node = current_node.next

    def search(self, data):
        """
        Search the target data in the linked list, and return the index of the target.
        If there is no such data in the linked list, return -1.
        :param data:
        :return:
        """
        current_node = self.__head
        index = 0
        while current_node is not None:
            if current_node.data == data:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def reverse_linked_list(self):
        """ Reverse this linked list. """
        if self.__head is None or self.__head.next is None:
            return self.__head
        prior_node, next_node = None, None
        current = self.__head
        while current:
            next_node = current.next        # Record the next node of current node.
            current.next = prior_node       # Reverse the point. Namely let the next node of the current node be its original prior node.
            prior_node = current            # Move the index to the next node.
            current = next_node             # Move the index to the next node.
        return prior_node       # Finally, the prior_node indicates the final node of the original Linked List.


class DoubleLinkedNode(object):
    """
    The node of the double linked list.
    """
    def __init__(self, data):
        self.data = data
        self.prior = None
        self.next = None


class DoubleLinkedList(object):
    """
    Double linked list.
    """
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def get_length(self):
        length = 0
        current_node = self.__head
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length

    def traverse(self):
        current_node = self.__head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def add(self, data):
        """
        Add data to the head of the list.
        :return:
        """
        temp_node = DoubleLinkedNode(data)
        if self.is_empty():
            self.__head = temp_node
        else:
            # Important!!!!
            temp_node.next = self.__head
            self.__head.prior = temp_node
            self.__head = temp_node

    def append(self, data):
        """
        Append data to the tail of the list.
        :return:
        """
        temp_node = DoubleLinkedNode(data)
        if self.is_empty():
            self.__head = temp_node
        else:
            current_node = self.__head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = temp_node
            temp_node.prior = current_node

    def insert(self, index, data):
        if index <= 0:
            self.add(data)
        elif index > self.get_length()-1:
            self.append(data)
        else:
            temp_node = DoubleLinkedNode(data)
            current_index = 0
            current_node = self.__head
            while current_index < index-1:
                current_index += 1
                current_node = current_node.next
            temp_node.next = current_node.next
            temp_node.prior = current_node
            current_node.next.prior = temp_node
            current_node.next = temp_node

    def remove(self, data):
        if self.is_empty():
            return
        current_node = self.__head
        # head is the target node.
        if current_node.data == data:
            # the list has only a head node
            if current_node.next is None:
                self.__head = None
            else:
                current_node.next.prior = None
                self.__head = current_node.next
            return
        while current_node is not None:
            if current_node.data == data:
                current_node.prior.next = current_node.next
                current_node.next.prior = current_node.prior
                break
            current_node = current_node.next

    def search(self, data):
        current_node = self.__head
        current_index = 0
        while current_node is not None:
            if current_node.data == data:
                return current_index
            current_index += 1
            current_node = current_node.next
        return -1

if __name__ == '__main__':
    a = DoubleLinkedList()
    a.add(0)
    a.append(1)
    a.append(3)
    print(a.traverse())
