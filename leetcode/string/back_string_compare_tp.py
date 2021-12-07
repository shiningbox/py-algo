from typing import List
from typing import Optional

class Solution:

    """ 1. Thoughts
        - from back to front
        - if count > 0 && == #, skip number of # characters
        - if count == 0, # has been skipped && current different, return false
        - if one ends, the other count == 0 && has any char return false
        - else return true"""
    def backspaceCompare(self, s, t):
        i, j = len(s) - 1, len(t) - 1
        bcount_s = 0
        bcount_t = 0
        # both strings are scanned
        while not (i < 0 and j < 0):
            # If need to skip #s
            # or the current character is #
            while i >= 0 and (bcount_s > 0 or s[i] == "#"):
                if s[i] == "#":
                    bcount_s += 1
                else:
                    bcount_s -= 1
                i -= 1
            s_char = '@' if i < 0 else s[i]
            while j >= 0 and (bcount_t > 0 or t[j] == "#"):
                if t[j] == "#":
                    bcount_t += 1
                else:
                    bcount_t -= 1
                j -= 1
            t_char = '@' if j < 0 else t[j]

            # if the backed char are not equal
            if s_char != t_char:
                return False
            # if equal, move to next char
            i -= 1
            j -= 1

        return True
def test():
    solution = Solution()
    # test method
    print(solution.backspaceCompare("a##j", "#a#j"))
    print(solution.backspaceCompare("a#j", "b"))


test()
