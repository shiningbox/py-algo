from typing import List

class Stack:

    def __init__(self):
        self.array = [None] * (10 ** 4)
        self.top_index = -1

    def size(self):
        return self.top_index + 1

    def pop(self):
        element = self.array[self.top_index]
        self.top_index -= 1
        return element

    def push(self, data):
        self.top_index += 1
        self.array[self.top_index] = data

    def top(self):
        return self.array[self.top_index]

class Solution:

    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False

        stack = Stack()
        p_dict = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            # If j is in the starting of the parentheses
            if c in p_dict.keys():
                stack.push(c)
            else:
                # Else, end of parentheses
                # Found a pair
                if stack.size() > 0 and p_dict[stack.top()] == c:
                    stack.pop()
                    continue
                else:
                    # Not a pair, early stop
                    return False
        return stack.size() == 0

def test():
    solution = Solution()
    # test method
    print(solution.isValid("(]"))
    print(solution.isValid("([)]"))
    print(solution.isValid("{[]}"))
    print(solution.isValid("}["))
    print(solution.isValid("}}["))
    print(solution.isValid("}"))


test()
