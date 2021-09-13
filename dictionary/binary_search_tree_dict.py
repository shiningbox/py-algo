from adt import Dictionary, DictionaryException
from tree.array_binary_tree import ArrayBinaryTree
from tree.adt import Tree, ArrayTreeNode,  TreeException
from priority_queue.adt import Item, Comparator


class BinarySearchTreeDict(Dictionary):

    # Binary search tree based dictionary
    def __init__(self):
        # Create an empty dict element as init root element
        root_item = Item(None, None)
        self.bt = ArrayBinaryTree(root_item, 5000)

    def size(self) -> int:
        pass

    def is_empty(self) -> bool:
        pass

    def empty(self) -> bool:
        root = self.bt.root()
        if root.element is None:
            return True

    # Find element in O(h) h is the height of the tree
    def find_element(self, key: object) -> object:

        if self.empty():
            return "Empty dict"

        root = self.bt.root()
        founded_node = self.binary_tree_search(key, root)

        if self.bt.is_external(founded_node):
            return "NO_SUCH_KEY"
        else:
            return founded_node.element.element

    def find_all_elements(self, key: object) -> list:
        pass

    def insert_item(self, key: object, element: object):
        # Find the starting_node to be inserted,
        # either the external starting_node,
        # or internal starting_node which has the key
        new_node_item = Item(key, element)
        root = self.bt.root()
        node_to_insert = self.binary_tree_search(key, root)
        # If key doesn't not exist after searching reaches to leaf

        # If there is a key already exists
        while self.bt.is_internal(node_to_insert):
            # Go to its right child
            node_to_insert = self.bt.right_child(node_to_insert)
            if self.bt.is_external(node_to_insert):
                    break
            # If found starting_node is still an internal starting_node, continue search
            node_to_insert = self.binary_tree_search(key, node_to_insert)

        # If it is an external starting_node
        if self.bt.is_external(node_to_insert):
            node_to_insert.element = new_node_item
            self.bt.expand_external(node_to_insert)

    # make sure no hole left in the tree after removal
    # thus, if it is an internal starting_node with two non-internal children
    # need to move its next starting_node (in inorder traverse) to fill its position
    def remove(self, key: object) -> object:
        # Find the starting_node to remove
        removal_node = self.binary_tree_search(key, self.bt.root())
        # If the starting_node is external starting_node
        if self.bt.is_external(removal_node):
            return "NO_SUCH_KEY"

        return_element = removal_node.element

        left_child = self.bt.left_child(removal_node)
        right_child = self.bt.right_child(removal_node)
        # If one of the tree starting_node is external starting_node
        if self.bt.is_external(left_child):
            removal_node = left_child
        elif self.bt.is_external(right_child):
            removal_node = right_child
        # If all tree starting_node are internal nodes
        else:
            # Keep the reference of the removal starting_node to be swapped
            swap_node = removal_node
            # Find the top left child of right child, which is the next element of inorder traverse
            removal_node = right_child
            while self.bt.is_internal(removal_node):
                removal_node = self.bt.left_child(removal_node)
            removal_node_parent = self.bt.parent(removal_node)
            self.bt.swap(swap_node, removal_node_parent)

        self.bt.remove_external_above(removal_node)
        return return_element

    def remove_all(self, key: object) -> list:
        pass

    def binary_tree_search(self, key: object, node: ArrayTreeNode):

        if self.bt.is_external(node):
            return node

        # If the starting_node's key equals the target key
        if node.element.key == key:
            return node

        # If the current starting_node's key less than the key, search its left child
        if key >= node.element.key:
            left_child = self.bt.right_child(node)
            return self.binary_tree_search(key, left_child)

        # If the current starting_node's key less than the key, search its left child
        if key < node.element.key:
            left_child = self.bt.left_child(node)
            return self.binary_tree_search(key, left_child)

    def print_dict_seq(self):
        root = self.bt.root()
        sequence = []
        self.bt.in_order(root, sequence)
        for node in sequence:
            if node.element is not None:
                print(f"{node.element.key}, {node.element.element}")
            pass

    def print_tree_structure(self):
        root = self.bt.root()
        self.bt.set_height(root)
        self.bt.print_subtree(root, prefix="")

def insert_balanced():
    dict = BinarySearchTreeDict()
    dict.insert_item(5, 'E')
    dict.insert_item(6, 'F')
    dict.insert_item(1, 'A')
    dict.insert_item(3, 'C')
    dict.insert_item(4, 'D')
    dict.insert_item(2, 'B')
    dict.insert_item(8, 'H')
    dict.insert_item(7, 'G')
    dict.insert_item(9, 'I')
    dict.insert_item(10, 'J')
    return dict

def insert_unbalanced():
    dict = BinarySearchTreeDict()
    dict.insert_item(10, 'J')
    dict.insert_item(9, 'I')
    dict.insert_item(8, 'H')
    dict.insert_item(7, 'G')
    dict.insert_item(6, 'F')
    dict.insert_item(5, 'E')
    dict.insert_item(4, 'D')
    dict.insert_item(3, 'C')
    dict.insert_item(2, 'B')
    dict.insert_item(1, 'A')
    return dict

def insert_unbalanced2():
    dict = BinarySearchTreeDict()
    dict.insert_item(44, 'D')
    dict.insert_item(17, 'B')
    dict.insert_item(32, 'C')
    dict.insert_item(78, 'I')
    dict.insert_item(50, 'F')
    dict.insert_item(48, 'E')
    dict.insert_item(62, 'H')
    dict.insert_item(54, 'G')
    dict.insert_item(88, 'J')
    return dict

def testing():
    dict = insert_unbalanced()
    dict.print_tree_structure()
    dict.remove(1)
    dict.remove(2)
    dict.remove(3)
    dict.remove(4)
    dict.print_dict_seq()
    dict.remove(5)
    dict.remove(6)
    dict.remove(7)
    dict.print_dict_seq()
    dict.remove(8)
    dict.remove(9)
    #dict.remove(10)
    #dict.print_dict()


def find_elements(dict):
    print("find keys 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
    print(dict.find_element(1))
    print(dict.find_element(2))
    print(dict.find_element(3))
    print(dict.find_element(4))
    print(dict.find_element(5))
    print(dict.find_element(6))
    print(dict.find_element(7))
    print(dict.find_element(8))
    print(dict.find_element(9))
    print(dict.find_element(10))


dict = insert_unbalanced2()
dict.print_tree_structure()
