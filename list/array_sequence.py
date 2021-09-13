from list.adt import Sequence, SequenceException, Position


class ArraySequence(Sequence):

    def __init__(self, capacity):
        self.sequence_size = 0
        self.capacity = capacity
        self.sequence = [None] * capacity

    def position_at_rank(self, rank: int) -> Position:

        if rank < 0 or rank > self.size():
            raise SequenceException("Out of bound exception")

        return self.sequence[rank]

    def rank_of_position(self, pos: Position) -> int:
        pass

    def swap(self, p: int, q: int):
        temp = self.sequence[p]
        self.sequence[p] = self.sequence[q]
        self.sequence[q] = temp

    def insert_first(self, element: object) -> object:
        pass

    def insert_before(self, pos: Position, element: object) -> object:
        pass

    def before(self, pos: Position) -> object:
        pass

    def after(self, pos: Position) -> object:
        pass

    def insert_after(self, pos: Position, element: object) -> object:
        pass

    def insert_last(self, element: object) -> object:
        self.sequence[self.size()] = element
        self.sequence_size += 1

    def first(self) -> object:
        pass

    def is_first(self, pos: Position) -> bool:
        pass

    def last(self) -> object:
        pass

    def is_last(self, pos: Position) -> bool:
        pass

    def remove(self, pos: Position) -> object:
        pass

    # O(1)
    def elem_at_rank(self, rank: int) -> object:

        if rank < 0 or rank > self.size():
            raise SequenceException("Out of bound exception")

        return self.sequence[rank]

    # O(1)
    def replace_elem_rank(self, rank: int, element: object) -> object:

        if rank < 0 or rank > self.size():
            raise SequenceException("Out of bound exception")

        self.sequence[rank] = element

    # O(n)
    def insert_elem_rank(self, rank: int, element: object):

        if rank < 0 or rank > self.size():
            raise SequenceException("Out of bound exception")

        # Move all elements after rank by 1, wont include rank
        for index in range(self.size(), rank, -1):
            self.sequence[index] = self.sequence[index-1]
        self.sequence[rank] = element
        self.sequence_size += 1

    # O(n)
    def remove_elem_rank(self, rank: int) -> object:

        if rank < 0 or rank > self.size():
            raise SequenceException("Out of bound exception")

        temp = self.sequence[rank]
        for index in range(rank, self.size() - 1, 1):
            self.sequence[index] = self.sequence[index + 1]
        self.sequence_size -= 1
        return temp

    def size(self) -> int:
        return self.sequence_size

    def is_empty(self) -> bool:
        return self.size() == 0

    def print(self):
        if not self.is_empty():
            for i in range(0, self.size(), 1):
                print(self.sequence[i])
        else:
            print("Empty Sequence")


def simple_testing():
    sequence = ArraySequence(10)
    sequence.print()
    try:
        sequence.insert_elem_rank(9, 1)
    except SequenceException:
        pass

    sequence.insert_elem_rank(0, 1)
    sequence.insert_elem_rank(1, 1)
    sequence.insert_elem_rank(2, 4)
    sequence.replace_elem_rank(2, 3)
    sequence.replace_elem_rank(1, 2)
    sequence.insert_elem_rank(3, 4)
    sequence.insert_elem_rank(4, 6)
    sequence.insert_elem_rank(5, 5)
    sequence.remove_elem_rank(4)
    sequence.print()
    print(f"Current sequence size {sequence.size()}")

    print("----")
    sequence.remove_elem_rank(0)
    sequence.remove_elem_rank(4)
    sequence.print()
    print(f"Current sequence size {sequence.size()}")

    print("----")
    sequence.remove_elem_rank(1)
    sequence.remove_elem_rank(2)
    sequence.print()

    print("----")
    print(f"Current sequence size {sequence.size()}")
    sequence.remove_elem_rank(3)
    sequence.print()
    print(f"Current sequence size {sequence.size()}")