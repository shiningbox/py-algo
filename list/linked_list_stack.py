from list.adt import Stack, StackException, Node


class LinkedListStack(Stack):

    def __init__(self):
        self.top_node = None
        self.stack_size = 0

    # O(1)
    def push(self, obj: object):
        new_node = Node()
        new_node.element = obj
        new_node.next = self.top_node
        self.top_node = new_node
        self.stack_size += 1

    # O(1)
    def pop(self) -> object:
        if not self.is_empty():
            temp = self.top_node
            self.top_node = self.top_node.next
            self.stack_size -= 1
            return temp.element
        else:
            raise StackException("Empty Stack, Can not pop")

    def size(self) -> int:
        return self.stack_size

    def is_empty(self) -> bool:
        return self.top_node is None

    def top(self) -> object:
        return self.top_node

    def print(self):
        if not self.is_empty():
            current_element = self.top()
            while True:
                # Move to next element
                current_element.print()
                current_element = current_element.next
                if current_element is None:
                    break
        else:
            print("Empty Stack")


stack = LinkedListStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print()
print(f"Stack size is {stack.size()}")
print(f"Top is {stack.top().element}")
# Pop twice
print(f"Pop: {stack.pop()}")
print(f"Pop: {stack.pop()}")
print(f"Stack size is {stack.size()}")
stack.print()
# Pop twice again
print(f"Pop: {stack.pop()}")
print(f"Pop: {stack.pop()}")
print(f"Stack size is {stack.size()}")
stack.print()
# Pop empty stack
print(f"Pop: {stack.pop()}")