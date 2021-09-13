from list.adt import Sequence, DLNode, SequenceException, Position


class RankSequence(Sequence):

    def swap(self, p: Position, q: Position):
        pass

    def insert_first(self, element: object) -> object:
        pass

    def insert_before(self, pos: Position, element: object) -> object:
        pass

    def insert_after(self, pos: Position, element: object) -> object:
        pass

    def insert_last(self, element: object) -> object:
        pass

    def first(self) -> object:
        pass

    def is_first(self) -> bool:
        pass

    def last(self) -> object:
        pass

    def is_last(self) -> bool:
        pass

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
        self.seq_size = 0

    # O(N)
    def elem_at_rank(self, rank: int) -> object:

        if rank == self.seq_size:
            return self.trailer

        if rank <= self.seq_size / 2:
            index = 0
            node = self.header.next
            # Hop till one starting_node before the rank
            # If sequence is empty, then rank at 0 should return trailer
            while index < rank:
                node = node.next
                index += 1
            return node
        else:
            index = self.seq_size - 1
            node = self.trailer.prev
            while index > rank:
                node = node.prev
                index -= 1
            return node

    def check_rank(self, rank: int):
        if rank < 0 or rank > self.size():
            raise SequenceException("Out of bound exception")

    # O(1)
    def replace_elem_rank(self, rank: int, element: object) -> object:
        self.check_rank(rank)
        current = self.elem_at_rank(rank)
        current.element = element

    # O(1)
    def insert_elem_rank(self, rank: int, element: object):
        if rank < 0 or rank > self.size():
            raise SequenceException("Out of bound exception")
        # current
        current = self.elem_at_rank(rank)
        # prev_node
        prev_node = current.prev
        new_node = DLNode(element, prev_node, current)
        current.prev = new_node
        prev_node.next = new_node
        self.seq_size += 1

    # O(1)
    def remove_elem_rank(self, rank: int) -> object:
        if rank < 0 or rank > self.size():
            raise SequenceException("Out of bound exception")
            # current
        current = self.elem_at_rank(rank)
        prev = current.prev
        next = current.next
        prev.next = next
        next.prev = prev
        return current

    def size(self) -> int:
        return self.seq_size

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

# Rank based sequence testing
sequence = RankSequence()
sequence.insert_elem_rank(0, 1)
sequence.insert_elem_rank(1, 2)
sequence.insert_elem_rank(2, 3)
sequence.insert_elem_rank(3, 3)
sequence.insert_elem_rank(4, 5)
sequence.replace_elem_rank(3, 4)
sequence.print()
print(f"Sequence size {sequence.size()}")
print("---")
sequence.insert_elem_rank(2, 7)
sequence.insert_elem_rank(3, 6)
sequence.print()
print(f"Sequence size {sequence.size()}")
sequence.remove_elem_rank(2)
sequence.remove_elem_rank(2)
sequence.print()
print(f"Sequence size {sequence.size()}")

# Rank sequence based bubble sorting
