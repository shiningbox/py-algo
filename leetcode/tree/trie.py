from typing import List
from typing import Optional


class TreeNode:

    def __init__(self):
        self.val = None
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        node.val = 1

    # Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False

        if node.val == 1:
            return True
        else:
            return False

    # Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
print(param_2)
param_2 = obj.search("app")
print(param_2)
param_2 = obj.startsWith("app")
print(param_2)
obj.insert("app")
param_2 = obj.search("app")
print(param_2)

# param_3 = obj.startsWith(prefix)
