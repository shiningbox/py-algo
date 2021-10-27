from list.adt import Deque, DLNode, DequeException


class DequeImpl(Deque):

    def __init__(self):
        self.header = DLNode(None, None, None)
        self.trailer = DLNode(None, None, None)
        self.header.prev = None
        # Header -> Trailer
        self.header.next = self.trailer
        # Header <- Trailer
        self.trailer.prev = self.header
        self.header.element = None
        self.trailer.element = None
        self.size = 0

    def insert_first(self, obj: object):
        # Header -> Second
        second = self.header.next
        # Create a new DLNode
        # new -> Second
        # Header <- new
        new_node = DLNode(obj, self.header, second)
        # Header -> new
        self.header.next = new_node
        # new <- second
        second.prev = new_node
        self.size += 1

    def first(self) -> object:
        return self.header.next.element

    def remove_first(self) -> object:
        if not self.is_empty():
            # Get starting_node to be removed from header
            second = self.header.next
            next = second.next
            # Header -> Next
            self.header.next = next
            # Header <- Next
            next.prev = self.header
            self.size -= 1
            return next
        else:
            raise DequeException("Empty Deque")

    def remove_last(self) -> object:
        if not self.is_empty():
            last = self.trailer.prev
            second_last = last.prev
            # second_last -> trailer
            second_last.next = self.trailer
            # second_last <- trailer
            self.trailer.prev = second_last
            self.size -= 1
            return last
        else:
            raise DequeException("Empty Deque")

    def insert_last(self, obj: object):
        second_last = self.trailer.prev
        # New -> trailer
        # second_last <- New
        new_node = DLNode(obj, second_last, self.trailer)
        # second_last -> New
        second_last.next = new_node
        # new <- left_prev
        self.trailer.prev = new_node
        self.size += 1

    def last(self) -> object:
        return self.trailer.prev.element

    def size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.header.next == self.trailer

    def print(self):
        if not self.is_empty():
            current_node = self.header.next
            while True:
                print(current_node.element)
                current_node = current_node.next
                if current_node == self.trailer:
                    break
        else:
            print("Empty Deque")


deque = DequeImpl()
deque.print()
deque.insert_first(2)
deque.insert_first(1)
deque.insert_first(1)
deque.insert_first(1)
deque.remove_first()
deque.remove_first()
deque.insert_last(3)
deque.insert_last(4)
deque.insert_last(5)
deque.insert_last(5)
deque.insert_last(5)
deque.remove_last()
deque.remove_last()
deque.print()

deque.remove_first()
deque.remove_last()
deque.remove_last()
deque.remove_last()
deque.remove_last()
deque.print()

deque.remove_first()
deque.remove_last()
