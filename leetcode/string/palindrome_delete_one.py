from typing import List
from typing import Optional

class Solution:

    def valid_palindrome(self, s, token):
        l = 0
        h = len(s) - 1
        while l < h:
            if s[l] != s[h]:
                if token > 0:
                    token = 0
                    return self.valid_palindrome(s[l+1:h + 1], 0) or self.valid_palindrome(s[l:h], 0)
                else:
                    return False
            l += 1
            h -= 1

        return True

    # Given a string s, return true if the s can be palindrome after deleting at most one character from it.
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return False
        else:
            return self.valid_palindrome(s, 1)


def test():
    solution = Solution()
    # test method
    print(solution.validPalindrome("a"))
    print(solution.validPalindrome("abba"))
    print(solution.validPalindrome("aba"))
    print(solution.validPalindrome("abac"))
    print(solution.validPalindrome("abc"))
    print(solution.validPalindrome("abca"))
    print(solution.validPalindrome("eeccccbebaeeabebccceea"))
    print(solution.validPalindrome("fxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxf"))
    print(solution.validPalindrome("cupuuuupucu"))

test()
