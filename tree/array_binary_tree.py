from tree.adt import Tree, ArrayTreeNode,  TreeException

# starting_node rank:
# p(origin_v) = 1 if origin_v is root
# p(origin_v) = 2p(u), origin_v is the left_stack child of u
# p(origin_v) = 2p(u) + 1, if origin_v is the right_stack child of u
# Wasting space, need at most 2**n+1 - 1 space


class ArrayBinaryTree:

    def __init__(self, root_element, capacity):
        self.capacity = capacity
        self.node_array = [None]*self.capacity
        root = ArrayTreeNode(root_element, 1, self)
        # Start with 1
        # i.e., zero internal starting_node
        self.node_array[1] = root

    def root(self) -> ArrayTreeNode:
        return self.node_array[1]

    def is_root(self, node: ArrayTreeNode) -> bool:
        return self.root() == node

    def is_internal(self, node: ArrayTreeNode) -> bool:
        return self.left_child(node) is not None and self.right_child(node) is not None

    def is_external(self, node: ArrayTreeNode) -> bool:
        return self.left_child(node) is None and self.right_child(node) is None

    def add_children(self, parent: ArrayTreeNode, element_left: object, element_right: object):
        child_rank = 2 * parent.rank
        left_child = ArrayTreeNode(element_left, child_rank, self)
        right_child = ArrayTreeNode(element_right, (child_rank+1), self)
        self.node_array[child_rank] = left_child
        self.node_array[child_rank + 1] = right_child

    def left_child(self, parent: ArrayTreeNode) -> ArrayTreeNode:
        child_rank = 2 * parent.rank
        return self.node_array[child_rank]

    def right_child(self, parent: ArrayTreeNode) -> ArrayTreeNode:
        child_rank = 2 * parent.rank + 1
        return self.node_array[child_rank]

    def parent(self, node: ArrayTreeNode) -> ArrayTreeNode:
        if self.is_root(node):
            return None
        parent_rank = int(node.rank / 2)
        return self.node_array[parent_rank]

    def children(self, node: ArrayTreeNode) -> list:
        return [self.left_child(node), self.right_child(node)]

    def pre_order(self, node: ArrayTreeNode, sequence: list):
        sequence.append(node)
        if self.is_internal(node):
            self.pre_order(self.left_child(node), sequence)
            self.pre_order(self.right_child(node), sequence)
        return sequence

    def in_order(self, node: ArrayTreeNode, sequence: list):
        if self.is_internal(node):
            self.in_order(self.left_child(node), sequence)
            sequence.append(node)
            self.in_order(self.right_child(node), sequence)
        else:
            sequence.append(node)
        return sequence

    def expand_external(self, node: ArrayTreeNode) -> ArrayTreeNode:
        if self.is_external(node):
            parent_rank = node.rank
            self.add_children(node, element_left=None, element_right=None)
            return node
        else:
            raise TreeException("Not an external tree starting_node")

    def remove_external_above(self, node: ArrayTreeNode) -> ArrayTreeNode:
        if self.is_external(node):
            parent = self.parent(node)
            temp = parent
            sibling = self.sibling(node)
            # First remove the starting_node
            self.node_array[node.rank] = None
            # Update the parent to be sibling
            self.move_up(sibling, parent.rank)
            return temp
        else:
            raise TreeException(f"Not an external tree starting_node for {node.element}")

    def sibling(self, node: ArrayTreeNode):
        parent = self.parent(node)
        if parent is None:
            raise TreeException("Root has no sibling")
        else:
            if node == self.left_child(parent):
                return self.right_child(parent)
            else:
                return self.left_child(parent)

    def swap(self, a: ArrayTreeNode, b: ArrayTreeNode):
        temp = a.element
        a.element = b.element
        b.element = temp

    @staticmethod
    def replace(node: ArrayTreeNode, element: object):
        node.element = element

    def move_up(self, node: ArrayTreeNode, new_rank: int):
        if self.is_external(node):
            old_rank = node.rank
            node.rank = new_rank
            self.node_array[new_rank] = node
            self.node_array[old_rank] = None
            return
        else:
            # If it is an internal starting_node, move its left_stack and right_stack child to new position on the upper level
            left_child = self.left_child(node)
            right_child = self.right_child(node)
            # Move the starting_node to its parent
            node.rank = new_rank
            self.node_array[new_rank] = node
            new_left_child_rank = new_rank * 2
            new_right_child_rank = new_rank * 2 + 1
            self.move_up(left_child, new_left_child_rank)
            self.move_up(right_child, new_right_child_rank)

    def set_height_depth(self, node: ArrayTreeNode, depth):
        # If starting_node is a leaf starting_node, return
        if self.is_internal(node):
            depth += 1
            for index, child in enumerate(self.children(node)):
                child.depth = depth
                self.set_height_depth(child, depth)
            child_heights = []
            for index, child in enumerate(self.children(node)):
                child_heights.append(child.height)
            # Check if the starting_node is balanced
            max_height = max(child_heights)
            node.height = max_height + 1
            max_difference = self.max_diff(child_heights)
            if max_difference > 1 or max_difference < -1:
                node.is_balanced = False
            else:
                node.is_balanced = True

    def set_height(self, node: ArrayTreeNode):
        self.set_height_depth(node, node.depth)

    def max_diff(self, arr):
        max_diff = arr[1] - arr[0]
        arr_size = len(arr)
        for i in range(0, arr_size):
            for j in range(i + 1, arr_size):
                if (arr[j] - arr[i] > max_diff):
                    max_diff = arr[j] - arr[i]

        return max_diff

    # O(n) time, just need to iterate each child starting_node, total is n-1 (excluding the root starting_node)
    def print_subtree(self, node: ArrayTreeNode, prefix: str):
        current_prefix = f"{prefix}"
        if node.element is not None:
            print(f"{current_prefix}{node.element.key}, height: {node.height}, {node.is_balanced}")
        else:
            print(f"{current_prefix}NONE, height: {node.height}")
        # If starting_node is a leaf starting_node, return
        if self.is_internal(node):
            current_prefix = f"-{prefix}"
            for index, child in enumerate(self.children(node)):
                self.print_subtree(child, current_prefix)


def simple_testing():
    tree = ArrayBinaryTree("Paper", 100)
    # Add root child
    root = tree.root()
    tree.add_children(root, "Chapter 1", "Chapter 2")
    # Add children of next level nodes
    l1_node = tree.left_child(root)
    tree.add_children(l1_node, "S1.1", "S1.2")
    r1_node = tree.right_child(root)
    tree.add_children(r1_node, "S2.1", "S2.2")

    r2_node = tree.right_child(r1_node)
    tree.add_children(r2_node, "S2.2.1", "S2.2.2")
    # tree.swap(tree.left_child(r2_node), tree.right_child(r2_node))

    print(f"Parent of S2.2 starting_node is {tree.parent(r2_node).element}")
    print(f"Sibling of S2.2 starting_node is {tree.sibling(r2_node).element}")

    pre_order_sequence = []
    pre_order_sequence = tree.pre_order(root, pre_order_sequence)
    print("Pre-order tree: ")
    for node in pre_order_sequence:
        print(f"{node.element} with rank {node.rank}")

    external_node = tree.left_child(r2_node)
    tree.expand_external(external_node)
    children = tree.children(external_node)
    print(f"External starting_node rank {external_node.element} with rank {external_node.rank}")
    for child in children:
        print(f"Child `{child.element}` with rank {child.rank}")

    print("Before remove")
    tree.print_subtree(tree.root())
    # Now, remove S2.2.2 which is an internal starting_node
    print("After remove s2.2.2")
    node_to_be_removed = tree.right_child(r2_node)
    tree.remove_external_above(node_to_be_removed)
    tree.print_subtree(tree.root())
    print("After remove s2.2.1 left_stack None")
    s221 = tree.right_child(r1_node)
    s221_left = tree.left_child(s221)
    tree.remove_external_above(s221_left)
    tree.print_subtree(tree.root())
    print("After remove s2.1")
    s21 = tree.left_child(tree.right_child(root))
    tree.remove_external_above(s21)
    tree.print_subtree(tree.root())
    print("After remove None, sibling of Chapter 1")
    none = tree.right_child(root)
    tree.remove_external_above(none)
    tree.print_subtree(tree.root())
    print("After remove s11 ")
    s12 = tree.right_child(tree.root())
    tree.remove_external_above(s12)
    tree.print_subtree(tree.root())

#simple_testing()
