class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.queue1:
            self.queue1 += [x]
        elif self.queue2:
            self.queue2 += [x]
        else:
            self.queue1 += [x]


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.queue1:
            while self.queue1:
                cur_num = self.queue1.pop(0)
                if not self.queue1:
                    return cur_num
                self.queue2 += [cur_num]
        elif self.queue2:
            while self.queue2:
                cur_num = self.queue2.pop(0)
                if not self.queue2:
                    return cur_num
                self.queue1 += [cur_num]
        else:
            return


    def top(self) -> int:
        """
        Get the top element.
        """
        if self.queue1:
            return self.queue1[-1]
        elif self.queue2:
            return self.queue2[-1]
        else:
            return


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if not self.queue1 and not self.queue2 else False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
