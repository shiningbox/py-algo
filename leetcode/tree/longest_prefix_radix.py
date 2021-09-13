from typing import List

class TNode:

    def __init__(self):
        self.data = None
        self.chd = None


class Solution:

    # O(nlogn)
    def longestCommonPrefix(self, strs: List[str]) -> str:

        str_lens = len(strs)
        if str_lens == 1:
            return strs[0]

        str0 = strs[0]
        root = TNode()
        node = root
        # Create the first prefix tree
        for c in str0:
            node.data = c
            node.chd = TNode()
            node = node.chd

        # For all other strings,
        # check if they will cut the previous prefix tree or extend it
        for wd in strs[1:]:
            node = root
            for c in wd:
                # If the node.val match c
                if node.data == c:
                    node = node.chd
                else:
                    break
            # Bottom of the tree
            node.data = None
            node.chd = None

        prefix = ''
        node = root
        while node.data:
            prefix += node.data
            node = node.chd
        return prefix

def test():
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    #print(solution.longestCommonPrefix(["dog", "racecar", "car"]))

    # test method


test()
