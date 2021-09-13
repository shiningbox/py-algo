from typing import List
from typing import Optional

class Solution:

    def lengthOfLastWord(self, s: str) -> int:

        if len(s) == 0:
            return 0

        start = 0
        for i in range(len(s)):
            if s[i] != ' ':
                if s[start] == ' ':
                    start = i
                word_length = i - start + 1
            else:
                start = i

        return word_length


def test():
    solution = Solution()
    # test method
    print(solution.lengthOfLastWord(""))
    print(solution.lengthOfLastWord("h"))
    print(solution.lengthOfLastWord("Hello World"))
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))
    print(solution.lengthOfLastWord("luffy is still joyboy"))


test()
