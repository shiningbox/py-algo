from list.adt import Sequence, Position, SequenceException


class LinkedSequence(Sequence):

    def __init__(self):
        self.header = Position(None, None, None, self)
        self.tail = Position(None, None, None, self)
        self.header.next = self.tail
        self.tail.prev = self.header
        self.seq_size = 0

    def check_rank(self, rank: int):
        if rank < 0 or rank > self.size():
            raise SequenceException("Out of bound exception")

    # Rank related methods
    def elem_at_rank(self, rank: int) -> object:
        if rank == self.seq_size:
            return self.tail.element

        if rank <= self.seq_size / 2:
            index = 0
            node = self.header.next
            # Hop till one starting_node before the rank
            # If sequence is empty, then rank at 0 should return trailer
            while index < rank:
                node = node.next
                index += 1
            return node.element
        else:
            index = self.seq_size - 1
            node = self.tail.prev
            while index > rank:
                node = node.prev
                index -= 1
            return node.element

    def replace_elem_rank(self, rank: int, element: object) -> object:
        self.check_rank(rank)
        current = self.elem_at_rank(rank)
        current.element = element

    def insert_elem_rank(self, rank: int, element: object):
        self.check_rank(rank)
        current = self.elem_at_rank(rank)
        # prev_node
        prev_node = current.prev
        new_node = Position(element, prev_node, current, self)
        current.prev = new_node
        prev_node.next = new_node
        self.seq_size += 1

    def remove_elem_rank(self, rank: int) -> object:
        self.check_rank(rank)
        current = self.elem_at_rank(rank)
        prev = current.prev
        next = current.next
        prev.next = next
        next.prev = prev
        self.seq_size -= 1
        return current

    def remove(self, pos: Position) -> object:
        self.check_position(pos)
        prev = pos.prev
        next = pos.next
        prev.next = next
        next.prev = prev
        self.seq_size -= 1
        return pos.element

    def swap(self, p: Position, q: Position):
        self.check_position(p)
        self.check_position(q)
        temp = p.element
        p.element = q.element
        q.element = temp

    def before(self, pos: Position) -> object:
        self.check_position(pos)
        prev = pos.prev
        if prev == self.header:
            raise SequenceException("Can not go past the beginning of the sequence")
        return prev

    def after(self, pos: Position) -> object:
        self.check_position(pos)
        next = pos.next
        if next == self.tail:
            raise SequenceException("Can not go past the end of the sequence")
        return next

    def insert_first(self, element: object) -> object:
        next = self.header.next
        new_pos = Position(element, self.header, next, self)
        self.header.next = new_pos
        next.prev = new_pos
        self.seq_size += 1
        return new_pos

    def first(self) -> object:
        return self.header.next

    def is_first(self, pos) -> bool:
        return self.header.next == pos

    def insert_before(self, pos: Position, element: object) -> object:
        if self.is_empty():
            raise SequenceException("Invalid position")
        elif self.is_first(pos):
            return self.insert_first(element)
        else:
            prev = pos.prev
            return self.insert_after(prev, element)

    def insert_after(self, pos: Position, element: object) -> object:
        self.check_position(pos)
        new_pos = Position(element, pos, pos.next, self)
        pos.next.prev = new_pos
        pos.next = new_pos
        self.seq_size += 1
        return new_pos

    def insert_last(self, element: object) -> object:
        prev_node = self.tail.prev
        new_pos = Position(element, prev_node, self.tail, self)
        prev_node.next = new_pos
        self.tail.prev = new_pos
        self.seq_size += 1
        return new_pos

    def last(self) -> object:
        return self.tail.prev

    def is_last(self, pos: Position) -> bool:
        return self.tail.prev == pos

    def size(self) -> int:
        return self.seq_size

    def is_empty(self) -> bool:
        return self.header.next == self.tail

    def check_position(self, pos: Position) -> object:
        if pos == self.header:
            raise SequenceException("Header is not a valid position")
        if pos == self.header:
            raise SequenceException("Tail is not a valid position")
        if pos.container != self:
            raise SequenceException("Position doesn't belong to this container")
        return pos

    def position_at_rank(self, rank: int) -> Position:
        self.check_rank(rank)
        current = self.header.next
        index = 0
        while index < rank:
            current = current.next
            index += 1
        return current

    def rank_of_position(self, pos: Position) -> int:
        self.check_position(pos)
        rank = 0
        current = self.header.next
        while current != pos:
            current = current.next
            rank += 1
        return rank

    def print(self):
        if not self.is_empty():
            current_node = self.header.next
            while True:
                print(current_node.element, end='->')
                current_node = current_node.next
                if current_node == self.tail:
                    break
            print("-")
        else:
            print("Empty Sequence")


def basic_testing():
    seq = LinkedSequence()
    seq.print()
    seq.insert_first(2)
    seq.insert_first(6)
    seq.insert_last(3)
    node1 = seq.insert_last(4)
    node_before_4 = seq.insert_before(node1, 'Before 4')
    node2 = seq.insert_last(5)
    node_after_5 = seq.insert_after(node2, 'After 5')
    seq.insert_last(1)
    seq.print()
    print(f"First and last: ")
    print(seq.first().element)
    print(seq.last().element)
    next = seq.first().next
    next_next = next.next
    try:
        header = seq.before(seq.first())
        tail = seq.after(seq.last())
    except SequenceException:
        print("Expected seq bound check")
        pass

    print(f"Next element to 1 is {next.element}")
    print(f"Next element to 2 is {next_next.element}")
    print(f"Previous element to 3 is {seq.before(next_next).element}")

    # Now swap the elements
    seq.swap(seq.first(), seq.last())
    # Remove redundant elements
    seq.remove(node_after_5)
    seq.remove(node_before_4)
    seq.remove(seq.last())
    seq.remove(seq.first())

    seq.insert_elem_rank(1, 2)
    seq.remove_elem_rank(1)

    seq.print()

    print(f"Rank at position 0 is {seq.rank_of_position(seq.position_at_rank(0))}")
    print(f"Rank at rank 2 is {seq.rank_of_position(seq.position_at_rank(2))}")

#basic_testing()
