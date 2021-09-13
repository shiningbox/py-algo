from list.adt import Position
from tree.array_binary_tree import ArrayBinaryTree, TreeException
from tree.adt import Tree, ArrayTreeNode
from priority_queue.adt import PriorityQueue, Comparator, Item, PriorityQueueException


class HeapPriorityQueue(PriorityQueue):

    def __init__(self):
        # Heavy ones on the bottom
        # Each internal starting_node of the tree stores a key and element
        # Key in children should always larger than its parent
        # A complete binary tree is complete meaning
        ## starting_node of i, 0<=i<=h-1, is 2**i nodes
        ## All internal nodes at h-1 should be at the left of the tree

        # Better to use array based binary tree to implement a heap because heap will not have much wasting spaces
        #
        self.bt = ArrayBinaryTree(None, 100)
        self.last_node = self.bt.root()

    def elem_at_rank(self, rank: int) -> object:
        pass

    def position_at_rank(self, rank: int) -> Position:
        pass

    def rank_of_position(self, pos: Position) -> int:
        pass

    def replace_elem_rank(self, rank: int, element: object) -> object:
        pass

    def swap(self, p: Position, q: Position):
        pass

    def insert_elem_rank(self, rank: int, element: object):
        pass

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
        pass

    def remove_elem_rank(self, rank: int) -> object:
        pass

    def first(self) -> object:
        pass

    def is_first(self, pos: Position) -> bool:
        pass

    def last(self) -> object:
        return self.last_node

    def is_last(self, pos: Position) -> bool:
        pass

    def remove(self, pos: Position) -> object:
        pass

    def size(self) -> int:
        pass

    def is_empty(self) -> bool:
        return self.bt.root().element is None

    # The key is to find insertion position z, an external starting_node to expand:
    ## In general z = n + 1, n is the number of internal nodes
    ## 1. If T is empty, z = root
    ## 2. If the last starting_node is the right-most starting_node on its level, i.e., completely full, then z is the left-most
    ## of the bottom level external starting_node
    ## 3. If not completely full, then z is the external starting_node right to the last_node
    # After expand_external(z), z becomes an internal starting_node and the last position
    # After insertion, the tree should be complete
    # up-heap-bubbling
    # But also need to satisfy heap-order property, if k(z) is less than its parent k(u)
    # we need to swap k(z) and k(u), and keep going up untill k(z) > k(u)
    def insert_item(self, key: object, element: object) -> object:
        # Key is to find the insertion position z (external starting_node) based on last internal starting_node
        item = Item(key, element)
        node_to_expand = None
        # If is empty
        if self.is_empty():
            node_to_expand = self.bt.root()
        else:
            rank = self.last_node.rank + 1
            node_to_expand = self.bt.node_array[rank]
        # Expand the external starting_node into internal starting_node
        self.last_node = self.bt.expand_external(node_to_expand)
        # Replace the expanded external starting_node with (key, value)
        self.bt.replace(node_to_expand, item)
        current_node = node_to_expand
        # Up-bubbling till root
        while self.bt.parent(current_node) is not None:
            parent = self.bt.parent(current_node)
            # If current starting_node's key is less than its parent
            if Comparator.is_less_than_equal_to(self.get_key(current_node), self.get_key(parent)):
                # Swap element between current starting_node and parent
                self.bt.swap(current_node, parent)
            # Go to above level and check again
            current_node = parent

        # Check heap property to see if need to swap between child and parent, if child is less than parent
        return node_to_expand

    def min_element(self) -> object:
        pass

    def min_key(self) -> object:
        pass

    def remove_min_element(self):

        if self.is_empty():
            return None

        element_to_remove = self.bt.root().element
        parent_node = self.bt.root()
        left_child = self.bt.left_child(parent_node)
        right_child = self.bt.right_child(parent_node)
        # Last internal starting_node
        last_node = self.last_node
        # If the tree has only root starting_node
        if self.bt.is_external(left_child) and self.bt.is_external(right_child):
            parent_node.element = None
            return element_to_remove

        # Swap last starting_node with root
        self.bt.swap(parent_node, last_node)

        # Remove last internal starting_node with its None child
        last_rank = self.last_node.rank
        last_none_child = self.bt.left_child(last_node)
        self.bt.remove_external_above(last_none_child)
        # Update last external starting_node to be the starting_node next to it
        self.last_node = self.bt.node_array[last_rank - 1]

        # Perform down-bubbling till leaf starting_node
        child_node = self.next_internal_node(parent_node)
        while child_node is not None:
            # If child starting_node's key is smaller than parent, swap
            if Comparator.is_less_than_equal_to(self.get_key(child_node), self.get_key(parent_node)):
                self.bt.swap(child_node, parent_node)
            parent_node = child_node
            child_node = self.next_internal_node(parent_node)

        return element_to_remove

    def next_internal_node(self, node: ArrayTreeNode):
        left_child = self.bt.left_child(node)
        right_child = self.bt.right_child(node)
        if self.get_key(left_child) is None and self.get_key(right_child) is None:
            return None

        # If the root's
        if self.bt.is_internal(left_child) and self.bt.is_external(right_child):
            current_node = left_child
        else:
            if Comparator.is_less_than_equal_to(self.get_key(left_child), self.get_key(right_child)):
                current_node = left_child
            else:
                current_node = right_child

        return current_node

    @staticmethod
    def get_key(node: ArrayTreeNode) -> object:
        if isinstance(node, ArrayTreeNode):
            element = node.element
            if element is not None:
                return element.key
            else:
                return None
        else:
            raise TreeException("Invalid tree starting_node type")

    @staticmethod
    def get_element(node: ArrayTreeNode) -> object:
        if isinstance(node, ArrayTreeNode):
            element = node.element
            if element is not None:
                return element.element
            else:
                return None
        else:
            raise TreeException("Invalid tree starting_node type")

    def print_subtree(self, node: ArrayTreeNode, prefix=""):
        current_prefix = f"-{prefix}"
        print(f"{current_prefix}{HeapPriorityQueue.get_key(node)}, {HeapPriorityQueue.get_element(node)}")
        # If starting_node is a leaf starting_node, return
        if self.bt.is_internal(node):
            for index, child in enumerate(self.bt.children(node)):
                self.print_subtree(child, current_prefix)


def init_heap():
    heap = HeapPriorityQueue()
    heap.insert_item(4, 'C')
    heap.insert_item(5, 'A')
    heap.insert_item(6, 'Z')
    heap.insert_item(15, 'K')
    heap.insert_item(9, 'F')
    heap.insert_item(7, 'Q')
    heap.insert_item(20, 'B')
    heap.insert_item(16, 'X')
    heap.insert_item(25, 'J')
    heap.insert_item(14, 'E')
    heap.insert_item(12, 'H')
    heap.insert_item(11, 'S')
    heap.insert_item(8, 'W')
    heap.print_subtree(heap.bt.root(), "")
    return heap


heap = init_heap()
print("Now insert 2 T...")
heap.insert_item(2, 'T')
heap.insert_item(5, 'Q')
heap.insert_item(13, 'O')
heap.print_subtree(heap.bt.root(), "")
print(heap.last().element.key)
element = heap.remove_min_element()

while element is not None:
    print(f"{element.key}, {element.element}")
    element = heap.remove_min_element()
