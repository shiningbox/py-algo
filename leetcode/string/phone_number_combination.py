from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children



class Solution:

    def __init__(self):
        self.letter_dict = {}

    def generate_phone_dict(self):
        letter_dict = {}
        a_index = ord('a')
        index = 2
        i = 0
        while i < 24:
            letters = []
            j = i
            if chr(j + a_index) == 'p' or chr(j + a_index) == 'w':
                for j in range(i, i + 4):
                    letters.append(chr(j + a_index))
                i += 4
            else:
                for j in range(i, i + 3):
                    letters.append(chr(j + a_index))
                i += 3
            letter_dict[str(index)] = letters
            index += 1

        return letter_dict

    def get_children(self, i, digits):
        if i <= len(digits) - 2:
            return self.letter_dict[digits[i + 1]]
        else:
            return None

    def pre_order_traversal(self, i, node, digits, indent):
        # Root
        if node:
            print(f"{indent}'{node}'")
        else:
            return
        indent = indent + "-"
        children = self.get_children(i, digits)
        if children:
            for child in children:
                self.pre_order_traversal(i+1, child, digits, indent)

    def get_paths(self, i, node, digits, path, paths):
        # Root
        if node:
            if node != '*':
                path += node
        else:
            return

        children = self.get_children(i, digits)
        if children:
            for child in children:
                self.get_paths(i+1, child, digits, path, paths)
        else:
            paths.append(str(path))

    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        self.letter_dict = self.generate_phone_dict()
        path = ""
        paths = []
        self.get_paths(-1, "*", digits, path, paths)
        return paths

def test():
    solution = Solution()
    # test method
    print(solution.letterCombinations("23"))
    print(solution.letterCombinations(""))

test()
