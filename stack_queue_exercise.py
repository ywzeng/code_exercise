# -*- coding: utf-8 -*-

"""
@author: zyw
@file: stack_queue_exercise.py
@time: 2021/1/7
"""

class Stack(object):
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def push(self, item):
        self.__items += [item]

    def pop(self):
        return self.__items.pop()

    def peek(self):
        """
        Return the item at the top of the stack.
        :return:
        """
        if self.is_empty():
            return None
        return self.__items[-1]

    def size(self):
        """
        Return the element num of the stack.
        :return:
        """
        return len(self.__items)


class Queue(object):
    """
    FIFO. [a, b, c, d], in which a is the head of the queue and d is the tail of the queue.
    """
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue += [item]

    def dequeue(self):
        return self.__queue.pop(0)

    def is_empty(self):
        return len(self.__queue) == 0

    def size(self):
        return len(self.__queue)


class Deque(object):
    def __init__(self):
        self.__deque = []

    def is_empty(self):
        return len(self.__deque) == 0

    def size(self):
        return len(self.__deque)

    def add_front(self, item):
        self.__deque.insert(0, item)

    def add_tail(self, item):
        self.__deque += [item]

    def remove_front(self):
        return self.__deque.pop(0)

    def remove_tail(self):
        return self.__deque.pop()

