from typing import List
from typing import Optional


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for c in s:
            if c not in char_count:
                char_count[c] = 1
            else:
                count = char_count[c]
                char_count[c] = count + 1
        has_middle = False
        length = 0
        for value in char_count.values():
            if value % 2 == 1:
                has_middle = True
                length += value // 2 * 2
            else:
                length += value
        if has_middle:
            length += 1

        return length

def test():
    solution = Solution()
    # test method
    print(solution.longestPalindrome("abccccdd"))
    print(solution.longestPalindrome("ccc"))


test()
