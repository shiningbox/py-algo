from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children


class Solution:

    letter_dict = {}
    paths = []

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

    def get_paths(self, idx, node, digits, path):

        # Root
        if node:
            if node != '*':
                path += node
        else:
            return

        if idx <= len(digits) - 1:
            # if digits is not none
            children = self.letter_dict[digits[idx]]
            for child in children:
                self.get_paths(idx+1, child, digits, path)
        else:
            self.paths.append(str(path))


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.letter_dict = self.generate_phone_dict()
        self.paths = []
        self.get_paths(0, "*", digits, "")

        return self.paths


def test():
    solution = Solution()
    # test method
    print(solution.letterCombinations("23"))
    print(solution.letterCombinations("234"))
    print(solution.letterCombinations(""))


test()
