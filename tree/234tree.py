from dictionary.sorted_array_dict import OrderedArrayDict
from linked_tree import LinkTree
from adt import Tree, LinkTreeNode, TreeException
from list.adt import Node


class Multiway24Tree(LinkTree):

    def __init__(self, root: LinkTreeNode):
        self.tree_root = root

    def empty_dict(self, node: LinkTreeNode):
        dict = node.element
        if dict is None:
            return True
        else:
            return dict.is_empty()

    def initial_dict(self, node: LinkTreeNode):
        node_dict = OrderedArrayDict()
        child = LinkTreeNode(element=None, parent=node, children=None, container=mutl_tree)
        node_dict.insert_last(2 ** 12, child)
        node.element = node_dict
        node.children = [child]

    def get_dict(self, node: LinkTreeNode):
        if node is not None:
            return node.element
        else:
            return None

    def insert(self, key: object):
        found_item, node = self.find(key)
        # if the key is not found till reached external node
        if found_item is None:
            # If the node's key dict is empty, add a max one first
            if self.empty_dict(node):
                self.initial_dict(node)
            node_dict = self.get_dict(node)
            # Then create a new external node as the child of the parent
            child = LinkTreeNode(element=None, parent=node, children=None, container=mutl_tree)
            self.children(node).append(child)
            # Insert the new key into the parent
            node_dict.insert_item(key, child)

            # Overflow, needs to split
            if len(node.children) == 5 and \
                    node_dict.size() == 5:
                # k0, k1, k2, k3, max
                # left = k0, k1
                # right = k3, max
                # parent = k2
                # Find the parent of node
                parent = self.parent(node)

                # If it is a root node already
                if parent is None:
                    # create a new root
                    new_root = LinkTreeNode(OrderedArrayDict(), None, [], None)
                    self.tree_root = new_root
                    parent = new_root
                else:
                    # parent already exist
                    pass

                # Create two new nodes
                left_child = LinkTreeNode(None, parent, [], None)
                self.initial_dict(left_child)
                # Insert the old (k0, v0), (k1, v1) into left node
                k0 = node_dict.element_at_i(0).key
                v0 = node_dict.element_at_i(0).element
                k1 = node_dict.element_at_i(1).key
                v1 = node_dict.element_at_i(1).element
                k2 = node_dict.element_at_i(2).key
                k3 = node_dict.element_at_i(3).key
                v3 = node_dict.element_at_i(3).element
                left_child.element.insert_item(k0, v0)
                left_child.children.append(v0)
                left_child.element.insert_item(k1, v1)
                left_child.children.append(v1)
                right_child = LinkTreeNode(None, parent, [], None)
                self.initial_dict(right_child)
                right_child.element.insert_item(k3, v3)
                right_child.children.append(v1)

                #
                parent.element.insert_item(k2, left_child)
                parent.children.append(left_child)
                parent.element.insert_item(2**10, right_child)
                parent.children.append(right_child)


    def find(self, key: object):

        node = self.root()
        found_item = None

        while not self.empty_dict(node):
            # node dict [(key1, node1), (key2, node2)]
            # dict item with key closest to key (key, node)
            dict = node.element
            closest_item = dict.closest_element_after(key)
            # if found item' key equals key in the current node's dict
            if closest_item.key == key:
                found_item = closest_item
                break
            else:
                # Move to child at the next level
                node = closest_item.element

        if found_item is not None:
            return found_item, node
        # If not found, meaning it is an external node just return its parent
        else:
            if self.is_root(node):
                return found_item, self.root()
            else:
                return found_item, self.parent(node)

    @staticmethod
    def print_dict(node: LinkTreeNode):
        dict = node.element
        if dict is not None and \
                isinstance(dict, OrderedArrayDict) \
                and not dict.is_empty():
            for i in range(dict.size()):
                dict_item = dict.array[i]
                print(f"{dict_item.key}", end=" ")
            print("")
        else:
            print("na")

    def print_subtree(self, node: LinkTreeNode, prefix: str, depth: int):
        current_prefix = f"-{prefix}"
        self.print_dict(node)
        # If starting_node is a leaf starting_node, return
        if self.is_internal(node):
            depth += 1
            for index, child in enumerate(self.children(node)):
                depth = self.print_subtree(child, current_prefix, depth)
        return depth


# e.g., the dict of root has 4 (k, node), 5 children
# 4  6  12  15  max
# v1 v2 v3  v4  v5
# If searching 5, 5 < 6 (v2) the smallest key that larger than 5 (closest)
# Go to v4
root = LinkTreeNode(None, None, None, None)
mutl_tree = Multiway24Tree(root)
mutl_tree.insert(6)
mutl_tree.insert(12)
mutl_tree.insert(15)
mutl_tree.insert(4)

mutl_tree.print_subtree(mutl_tree.root(), "", 0)
#print(mutl_tree.print_dict(mutl_tree.find(5)[1]))
#print(mutl_tree.find(0))
#print(mutl_tree.print_dict(mutl_tree.find(12)[1]))
#print(mutl_tree.find(15))


