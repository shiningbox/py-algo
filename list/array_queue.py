from list.adt import Queue, QueueFullException


class ArrayQueue(Queue):

    def __init__(self, capacity):
        self.capacity = capacity + 1
        # Max size is self.capacity - 1
        self.q = [None] * self.capacity
        # The index of queue front
        self.f = 0
        # End of the queue, next available index for enqueue
        self.r = 0

    def enqueue(self, obj: object):
        if self.size() < self.capacity - 1:
            self.q[self.r] = obj
            self.r = (self.r + 1) % self.capacity
        else:
            raise QueueFullException("Queue is full, can not enqueue anymore")

    def dequeue(self) -> object:
        if not self.is_empty():
            # Get the current front
            temp = self.q[self.f]
            self.q[self.f] = None
            self.f = (self.f + 1) % self.capacity
            return temp

    def size(self) -> int:
        # Get Queue size
        # It is a circular array, when:
        # h >= f: e.g., capacity = 5, h = 3, f = 0, then the size is 5 + 3 % 5 = 3
        # h <= f: e.g., capacity = 5, h = 1, f = 3, then the size is 5 + 1 - 3 % 5 = 3
        return (self.capacity + self.r - self.f) % self.capacity

    def front(self) -> object:
        if not self.is_empty():
            return self.q[self.f]

    def is_empty(self) -> bool:
        return self.f == self.r

    def print(self):
        start = self.f
        while start != self.r:
            print(self.q[start])
            start = (start + 1) % self.capacity


def simple_test():
    queue = ArrayQueue(4)
    queue.enqueue('first')
    queue.enqueue('second')
    queue.enqueue('third')
    queue.enqueue('fourth')
    print(f"Front is '{queue.front()}'")
    print(f"Size is {queue.size()}")
    queue.print()

    print("Dequeue the first element...")
    queue.dequeue()
    queue.enqueue('fifth')
    print(f"Front is '{queue.front()}'")
    print(f"Size is {queue.size()}")
    queue.print()

    print("Dequeue the second element...")
    queue.dequeue()
    queue.enqueue('sixth')
    print(f"Front is '{queue.front()}'")
    print(f"Size is {queue.size()}")
    queue.print()
    queue.enqueue('seventh')
