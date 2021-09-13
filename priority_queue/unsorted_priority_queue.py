from list.adt import Position
from priority_queue.adt import PriorityQueue, Item, PriorityQueueException
from list.linked_sequence import LinkedSequence


class UnsortedPriorityQueue(LinkedSequence, PriorityQueue):

    # O(1) for unsorted, insert to the last
    # O(n) for sorted
    def insert_item(self, key: object, element: object):
        new_item = Item(key, element)
        self.insert_last(new_item)

    # O(n) for unsorted
    # O(1) for sorted
    def min_element(self) -> Position:
        if not self.is_empty():
            current_node = self.header.next
            min_node = current_node
            min_key = current_node.element.key
            while True:
                current_node = current_node.next
                if current_node == self.tail:
                    break
                else:
                    current_key = current_node.element.key
                    if current_key <= min_key:
                        min_key = current_key
                        min_node = current_node
        else:
            print("Empty Sequence")
            min_node = None
        return min_node

    # O(n) for unsorted
    # O(1) for sorted
    def min_key(self):
        return self.min_element().element.key

    # O(n) for unsorted
    # O(1) for sorted
    def remove_min_element(self) -> Position:
        min_node = self.min_element()
        min_position = self.remove(min_node)
        return min_position

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

    # Select the minimal at a time
    # Worst-cast O(n**2) time and always will be O(n**2) because it needs to iterate entire input sequence everything
    # in order to find the min value
    def selection_sort(self):
        results = []
        for i in range(self.seq_size):
            results.append(self.remove_min_element().element.key)
        return results


def basic_testing():
    seq = UnsortedPriorityQueue()
    seq.print()
    seq.insert_item(6, 4)
    seq.insert_item(0, 1)
    seq.insert_item(2, 2)
    seq.insert_item(5, 3)
    seq.insert_item(7, 5)
    seq.print()
    print(f"Min key is {seq.min_key()}")
    print(f"Min Element is {seq.min_element().element.element}")
    print(f"Min Element to be removed {seq.remove_min_element().element.element}")
    seq.print()

    sorted_result = seq.selection_sort()
    for result in sorted_result:
        print(result)


#basic_testing()