from typing import List
from typing import Optional


class Solution:

    """
    - Two stacks, one stores (, another stores )
    -- Since two stacks store the same elements, we can use count to represent stack
    -- 3 means (((
    -- 3 means )))

    - Generate a binary tree from the two stacks by poping from the two stacks
    When two stacks are empty, we have a output string


    For the output string to be validated, stack of ")" must be larger than stack of "(".
    If not, it creates string like "())"
    """

    def generateParenthesis(self, n):
        if not n:
            return []
        l_stack, r_stack, res = n, n, []
        self.dfs(l_stack, r_stack, res, "")
        return res

    def dfs(self, left_stack, right_stack, res, string):
        if right_stack < left_stack:
            return
        if not left_stack and not right_stack:
            res.append(string)
            return
        if left_stack:
            self.dfs(left_stack - 1, right_stack, res, string + "(")
        if right_stack:
            self.dfs(left_stack, right_stack - 1, res, string + ")")


def test():
    solution = Solution()
    # test method
    print(solution.generateParenthesis(3))

test()
