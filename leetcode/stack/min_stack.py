from typing import List
from typing import Optional


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [None] * 30000
        self.top_index = -1
        self.size = 0

    def push(self, val: int) -> None:
        min_value = val
        # Empty stack
        if self.top_index != -1:
            min_value = self.getMin()
            if val <= min_value:
                min_value = val
        self.top_index += 1
        self.stack[self.top_index] = (val, min_value)
        self.size += 1

    def pop(self) -> None:
        val, _ = self.stack[self.top_index]
        self.top_index -= 1
        self.size -= 1
        return val

    def top_tuple(self):
        return self.stack[self.top_index]

    def top(self) -> int:
        return self.top_tuple()[0]

    def getMin(self) -> int:
        return self.top_tuple()[1]

    def print_stack(self):
        for i in range(self.size):
            print(self.stack[i], end=' ')

def test():
    stack = MinStack()
    # test method
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    stack.push(4)
    stack.push(5)
    print(stack.getMin())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.getMin())
    print(stack.top())
    stack.print_stack()

test()
