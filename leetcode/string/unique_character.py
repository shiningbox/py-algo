from typing import List
from typing import Optional

class Solution:

    def firstUniqChar(self, s: str) -> int:
        char_dict = [None] * 26
        for char in s:
            index = ord(char) - ord('a')

            if not char_dict[index]:
                char_dict[index] = 1
            else:
                val = char_dict[index]
                char_dict[index] = val + 1

        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if char_dict[index] and char_dict[index] == 1:
                return i

        return -1


def test():
    solution = Solution()
    # test method
    print(solution.firstUniqChar("leetcode"))
    print(solution.firstUniqChar("aabbc"))


test()
