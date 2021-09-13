from list.adt import Stack, StackException


class ArrayStack(Stack):

    def __init__(self):
        # A list represents
        self.s = []
        # top index
        self.top_index = -1
        # initial a list with NaN values
        self.s = [None] * 1000

    def push(self, obj: object):
        self.top_index += 1
        self.s[self.top_index] = obj

    def pop(self) -> object:
        if not self.is_empty():
            top_element = self.s[self.top_index]
            self.top_index -= 1
            return top_element
        else:
            raise StackException("Stack is empty")

    def size(self) -> int:
        return self.top_index + 1

    def is_empty(self) -> bool:
        return self.top_index < 0

    def top(self) -> object:
        if self.top_index > 0:
            return self.s[self.top_index]

    def print(self):
        # If not empty, print all element
        if not self.is_empty():
            for index in range(self.size()):
                print(self.s[index])
        else:
            print("Empty stack")


stack = ArrayStack()
stack.push(1)
stack.push(2)
stack.push('3')
print(f"Stack Size is {stack.size()}")
stack.print()
stack.pop()
stack.pop()
stack.pop()
print(f"Stack Size is {stack.size()}")
stack.print()
