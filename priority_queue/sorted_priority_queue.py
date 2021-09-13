from list.adt import Position
from priority_queue.adt import PriorityQueue, Comparator, Item, PriorityQueueException
from list.linked_sequence import LinkedSequence


class LinkedSortedPriorityQueue(LinkedSequence, PriorityQueue):

    @staticmethod
    def get_key(node):
        if isinstance(node.element, Item):
            return node.element.key
        else:
            raise Exception("Not a item")

    # O(n) for sorted
    # O(n**2) for inserting n elements
    def insert_item(self, key: object, element: object):
        new_item_element = Item(key, element)
        # If the seq is empty, then O(1) insert to the first element
        if self.is_empty():
            self.insert_first(new_item_element)
        # If the key is larger than the last key (largest key)
        elif Comparator.is_greater_than_equal_to(key, LinkedSortedPriorityQueue.get_key(self.last())):
            self.insert_last(new_item_element)
        # Else,
        else:
            current_node = self.header.next
            # Find the first one larger than the new element, then insert it before that element
            while Comparator.is_greater_than_equal_to(key, self.get_key(current_node)):
                current_node = current_node.next
                if current_node == self.tail:
                    break
            self.insert_before(current_node, new_item_element)

    # O(n) for unsorted
    # O(1) for sorted
    def min_element(self) -> Position:
        return self.first()

    # O(n) for unsorted
    # O(1) for sorted
    def min_key(self):
        return self.get_key(self.first())

    # O(n) for unsorted
    # O(1) for sorted
    def remove_min_element(self) -> Position:
        return self.remove(self.first())

    def print(self):
        if not self.is_empty():
            current_node = self.header.next
            while True:
                print(f"Key is: {current_node.element.key}, Element is: {current_node.element.element}")
                current_node = current_node.next
                if current_node == self.tail:
                    break
        else:
            print("Empty Sequence")

    # Remove the min-one, which is the first position
    # Worst-case O(n**2) if
    # Best-case O(n)
    def insert_sort(self):
        results = []
        for i in range(self.seq_size):
            results.append(self.remove_min_element().element.key)
        return results


def basic_testing():
    seq = LinkedSortedPriorityQueue()
    seq.print()
    seq.insert_item(6, 1)
    seq.insert_item(0, 4)
    seq.insert_item(2, 2)
    seq.insert_item(1, 3)
    seq.insert_item(3, 5)
    seq.insert_item(4, 7)
    seq.insert_item(4, 9)
    seq.insert_item(5, 8)
    seq.print()

    print(f"Min key is {seq.min_key()}")
    print(f"Min Element is {seq.min_element().element.element}")
    print(f"Min Element to be removed {seq.remove_min_element().element.element}")
    seq.print()


#basic_testing()