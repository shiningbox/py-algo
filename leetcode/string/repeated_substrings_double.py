from typing import List
from typing import Optional

class Solution:

    #O(n2)
    def repeatedSubstringPattern(self, s):
        """
        :type str: str
        :rtype: bool
        """
        if not s:
            return False
        # s will have at least two repeated substrings
        # double s will make it at least four repeated substrings
        # Now we break the first and last character
        ss = (s + s)[1:-1]
        return ss.find(s) != -1

def test():
    solution = Solution()
    # test method
    print(solution.repeatedSubstringPattern("abcdef"))
    print(solution.repeatedSubstringPattern("aaaa"))
    print(solution.repeatedSubstringPattern("abab"))
    print(solution.repeatedSubstringPattern("abcabcabc"))
    print(solution.repeatedSubstringPattern("abcbcabc"))
    print(solution.repeatedSubstringPattern("a"))
    print(solution.repeatedSubstringPattern("abaababaab"))
    print(solution.repeatedSubstringPattern("ababababab"))
    print(solution.repeatedSubstringPattern("abac"))
    print(solution.repeatedSubstringPattern("babbabbabbabbab"))


test()
