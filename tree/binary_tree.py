from linked_tree import LinkTree
from adt import Tree, LinkTreeNode, TreeException


# External nodes is 1 more than internal nodes
## Repeating remove above external starting_node (while it is still a proper binary tree), till to the root
## Then remove one of the two child starting_node, then left only one external starting_node
# level d has at most 2d nodes
class LinkedBinaryTree(LinkTree):

    def __init__(self, tree_root: LinkTreeNode):
        super(LinkedBinaryTree, self).__init__(tree_root)

    def left_child(self, parent: LinkTreeNode) -> LinkTreeNode:
        children = self.children(parent)
        if len(children) != 2:
            raise TreeException("Not a proper binary tree")
        return children[0]

    def right_child(self, parent: LinkTreeNode) -> LinkTreeNode:
        children = self.children(parent)
        if len(children) != 2:
            raise TreeException("Not a proper binary tree")
        return children[1]

    def expand_external_node(self, node: LinkTreeNode):
        pass

    def remove_above_external_node(self, node: LinkTreeNode):
        pass

    # Parent->Left->Right
    def pre_order(self, node: LinkTreeNode, sequence: list):
        sequence.append(node)
        if self.is_internal(node):
            self.pre_order(self.left_child(node), sequence)
            self.pre_order(self.right_child(node), sequence)
        return sequence

    # Left->Right->Parent
    def post_order(self, node: LinkTreeNode, sequence: list):
        if self.is_internal(node):
            self.post_order(self.left_child(node), sequence)
            self.post_order(self.right_child(node), sequence)
        sequence.append(node)
        return sequence

    # Left->Right->Parent
    def evaluate_expression(self, node: LinkTreeNode):
        value1 = 0
        value2 = 0
        # If it is an operator internal starting_node
        if self.is_internal(node) and node.element in ['*', '/', '+', '-']:
            value1 = self.evaluate_expression(self.left_child(node))
            value2 = self.evaluate_expression(self.right_child(node))
            return evaluate(node.element, value1, value2)
        # If it is a value external starting_node
        else:
            return float(node.element)

    # Create a non-decreasing sequence
    def in_order(self, node: LinkTreeNode, sequence: list):
        if self.is_internal(node):
            self.in_order(self.left_child(node), sequence)
            sequence.append(node)
            self.in_order(self.right_child(node), sequence)
        else:
            sequence.append(node)
        return sequence


def evaluate(operator: str, value1: float, value2: float) -> float:
    if operator == '*':
        return value1 * value2
    if operator == '-':
        return value1 - value2
    if operator == '+':
        return value1 + value2
    if operator == '/':
        return value1 / value2


def binary_tree_testing():
    root = LinkTreeNode("-", None, None, Tree)
    # First level
    node11 = LinkTreeNode("/", root, None, Tree)
    node12 = LinkTreeNode("+", root, None, Tree)
    tree = LinkedBinaryTree(root)
    tree.set_children(root, [node11, node12])
    # Second level
    node21 = LinkTreeNode("*", node11, None, Tree)
    node22 = LinkTreeNode("+", node11, None, Tree)
    tree.set_children(node11, [node21, node22])

    node23 = LinkTreeNode("*", node12, None, Tree)
    node24 = LinkTreeNode("6", node12, None, Tree)
    tree.set_children(node12, [node23, node24])

    # Third level
    node31 = LinkTreeNode("4", node21, None, Tree)
    node32 = LinkTreeNode("3", node21, None, Tree)
    tree.set_children(node21, [node31, node32])

    node33 = LinkTreeNode("14", node22, None, Tree)
    node34 = LinkTreeNode("2", node22, None, Tree)
    tree.set_children(node22, [node33, node34])

    node35 = LinkTreeNode("3", node23, None, Tree)
    node36 = LinkTreeNode("3", node23, None, Tree)
    tree.set_children(node23, [node35, node36])

    print("Left and right children of node12 is: ")
    print(tree.left_child(node12).element)
    print(tree.right_child(node12).element)

    pre_order_sequence = []
    pre_order_sequence = tree.pre_order(root, pre_order_sequence)
    print("Pre-order binary tree: ")
    # for starting_node in pre_order_sequence:
    #    print(starting_node.element)

    print("Post-order binary tree: ")
    post_order_sequence = []
    post_order_sequence = tree.post_order(root, post_order_sequence)
    #for starting_node in post_order_sequence:
    #    print(starting_node.element)

    print(f"Evaluation result: {tree.evaluate_expression(root)}")


def binary_search_tree_testing():
    root = LinkTreeNode("50", None, None, Tree)
    # First level
    node11 = LinkTreeNode("25", root, None, Tree)
    node12 = LinkTreeNode("75", root, None, Tree)
    tree = LinkedBinaryTree(root)
    tree.set_children(root, [node11, node12])

    # Second level
    node21 = LinkTreeNode("10", node11, None, Tree)
    node22 = LinkTreeNode("30", node11, None, Tree)
    tree.set_children(node11, [node21, node22])

    node23 = LinkTreeNode("60", node12, None, Tree)
    node24 = LinkTreeNode("80", node12, None, Tree)
    tree.set_children(node12, [node23, node24])

    # Third level
    node31 = LinkTreeNode("78", node24, None, Tree)
    node32 = LinkTreeNode("90", node24, None, Tree)
    tree.set_children(node24, [node31, node32])

    tree.print_subtree(root, "", 0)

    print("In-order binary tree: ")
    in_order_sequence = []
    in_order_sequence = tree.in_order(root, in_order_sequence)
    for node in in_order_sequence:
        print(node.element)


binary_search_tree_testing()
