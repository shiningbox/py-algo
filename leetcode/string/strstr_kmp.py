from typing import List
from typing import Optional

class Solution:

    def failure_function(self, pattern: str) -> list:
        p_length = len(pattern)
        failure = [0] * p_length
        # Compare pattern with pattern itself
        i = 1
        j = 0

        while i < p_length:
            if pattern[i] == pattern[j]:
                # j represented the matched prefix before i
                failure[i] = j + 1
                i += 1
                j += 1
            # if not matched and j > 0 meaning there are previously matched P
            # check prefix f(j - 1) for a jump
            elif j > 0:
                j = failure[j - 1]
            else:
                # if not matched and j = 0 meaning the beginning of the pattern
                # then mark f[i] = 0
                # move to next i
                failure[i] = 0
                i += 1

        return failure

    def strStr(self, haystack: str, needle: str) -> int:

        if not haystack and not needle:
            return 0

        if len(needle) == 0:
            return 0

        if len(needle) > len(haystack):
            return -1

        j = 0
        i = 0

        failure = self.failure_function(needle)
        while i < len(haystack):
            # If match, continue index by 1
            if haystack[i] == needle[j]:
                if j == len(needle) - 1:
                    # a b j d
                    #     j d
                    return i - len(needle) + 1
                i += 1
                j += 1
            elif j > 0:
                j = failure[j - 1]
            else:
                i += 1
        return -1


def test():
    solution = Solution()
    # test method
    print(solution.strStr("test", "st"))
    print(solution.strStr("aaaaa", "bba"))
    print(solution.strStr("hello", "ll"))
    print(solution.strStr("mississippi", "issipi"))
    print(solution.strStr("", ""))

test()
