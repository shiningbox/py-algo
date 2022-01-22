from typing import List
from typing import Optional


class TreeNode:

    def __init__(self):
        self.val = None
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        node.val = 1

    def search_rec(self, root, word: str) -> bool:
        node = root
        i = 0
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    res = self.search_rec(child, word[i+1:])
                    if res:
                        return True
                return False
            if c in node.children:
                node = node.children[c]
            else:
                return False
            i += 0

        if node.val == 1:
            return True
        else:
            return False

    # Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    def search(self, word: str) -> bool:
        return self.search_rec(self.root, word)


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) # return False
print(wordDictionary.search("bad")) # return True
print(wordDictionary.search(".ad")) # return True
print(wordDictionary.search("b..")) # return True