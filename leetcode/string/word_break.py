from typing import List
from typing import Optional


class Node:
    def __init__(self):
        self.children = {}  # mapping from character to Node
        self.value = None
        self.visited = False

class Trie:

    def insert(self, node: Node, key: str, value) -> None:
        for char in key:
            # Create a new node
            if char not in node.children:
                node.children[char] = [Node()]
            else:
                node.children[char].append(Node())
            # Move to next
            node = node.children[char][-1]
        node.value = value

    def find(self, node: Node, key: str):
        """Find value by key in node."""
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.value

    def print_tires(self, node, indent):

        if not node:
            return None

        if not node.children:
            return None

        str_val = "".join(node.children.keys())
        print(indent + str_val)

        for key in node.children.keys():
            for child in node.children[key]:
                self.print_tires(child, indent + "-")

class Solution:

    def __init__(self):
        self.root = None

    def dfs_find(self, root, s_array):
        node = root
        print(s_array)
        while s_array:
            char = s_array.pop(0)
            if not node.children.keys():
                    node = self.root

            if char in node.children:
                nodes = node.children[char]
                for node in nodes:
                    if not node.visited:
                        node.visited = True
                        res = self.dfs_find(node, list(s_array))
                        if res:
                            return True
            else:
                return False

        return True

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        root = Node()
        self.root = root
        # Create a prefix tree
        for word in wordDict:
            trie.insert(self.root, word, "1")
        s_array = list(s)
        return self.dfs_find(self.root, s_array)


def test():
    solution = Solution()
    # test method
    #print(solution.wordBreak("applepenapple", ["apple", "pen"]))
    #print(solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
    #print(solution.wordBreak("abcd", ["a","abc","b","cd"]))
    print(solution.wordBreak("aaaaaaa", ["aaaa","aa"]))

test()
