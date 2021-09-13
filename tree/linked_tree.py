from adt import Tree, LinkTreeNode, TreeException


class LinkTree(Tree):

    def __init__(self, tree_root: LinkTreeNode):
        self.tree_root = tree_root

    def root(self) -> LinkTreeNode:
        return self.tree_root

    def parent(self, node: LinkTreeNode) -> LinkTreeNode:
        return node.parent

    def is_root(self, node: LinkTreeNode) -> bool:
        return node == self.tree_root

    def is_internal(self, node: LinkTreeNode) -> bool:
        return node.children is not None

    def is_external(self, node: LinkTreeNode) -> bool:
        return node.children is None

    def children(self, node: LinkTreeNode) -> list:
        return node.children

    def set_children(self, node: LinkTreeNode, children: list):
        node.children = children

    def size(self) -> int:
        pass

    def is_empty(self) -> bool:
        return self.children(self.root()) is None

    def elements(self) -> list:
        pass

    def nodes(self) -> list:
        pass

    def swap(self, node1: LinkTreeNode, node2: LinkTreeNode):
        temp = node1.element
        node1.element = node2.element
        node2.element = temp

    def replace(self, node: LinkTreeNode, element: object):
        node.element = element

    # O(n) time, just need to iterate each child starting_node, total is n-1 (excluding the root starting_node)
    def print_subtree(self, node: LinkTreeNode, prefix: str, depth: int):
        current_prefix = f"-{prefix}"
        print(f"{current_prefix}{node.element}")
        # If starting_node is a leaf starting_node, return
        if self.is_internal(node):
            depth += 1
            for index, child in enumerate(self.children(node)):
                depth = self.print_subtree(child, current_prefix, depth)
        return depth

    # O(n) Preorder traversal, parent-child root->n1>n11>n12
    # Can be used to display a document, extending from table of content
    def pre_order(self, node: LinkTreeNode, sequence: list):
        sequence.append(node)
        if self.is_internal(node):
            for index, child in enumerate(self.children(node)):
                sequence = self.pre_order(child, sequence)
        return sequence

    # O(n), Postorder n11>n12>n1>root
    # Can be used to aggregate child numbers such as file sizes
    def post_order(self, node: LinkTreeNode, sequence: list):
        if self.is_internal(node):
            child_enum = enumerate(node.children)
            next_child = next(child_enum, None)
            while next_child is not None:
                sequence = self.post_order(next_child[1], sequence)
                #  If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.
                next_child = next(child_enum, None)
        sequence.append(node)
        return sequence


def simple_testing():
    root = LinkTreeNode("Paper", None, None, Tree)
    node1 = LinkTreeNode("Charter 1", root, None, Tree)
    node2 = LinkTreeNode("Charter 2", root, None, Tree)
    tree = LinkTree(root)
    tree.set_children(root, [node1, node2])

    node3 = LinkTreeNode("S1.1", node1, None, Tree)
    node4 = LinkTreeNode("S1.2", node1, None, Tree)
    tree.set_children(node1, [node3, node4])

    node5 = LinkTreeNode("S2.1", node2, None, Tree)
    tree.set_children(node2, [node5])
    node6 = LinkTreeNode("S2.2.1", node5, None, Tree)
    tree.set_children(node5, [node6])

    print(f"if root is the tree root: {tree.is_root(root)}")
    print(f"if node1 is internal: {tree.is_internal(node1)}")
    print(f"if node2 is external: {tree.is_external(node2)}")
    print(f"if node3 is external: {tree.is_external(node3)}")
    print(f"if node4 is internal: {tree.is_internal(node4)}")

    print("Entire tree is: ")
    depth = tree.print_subtree(root, "", 1)
    print(f"Tree height is {depth}")
    depth = tree.print_subtree(node1, "", 0)
    print(f"Tree depth for node1 is {depth}")

    pre_order_sequence = []
    pre_order_sequence = tree.pre_order(root, pre_order_sequence)
    print("Pre-order tree: ")
    for node in pre_order_sequence:
        print(node.element)

    print("Post-order tree: ")
    post_order_sequence = []
    post_order_sequence = tree.post_order(root, post_order_sequence)
    for node in post_order_sequence:
        print(node.element)


#simple_testing()
