from typing import List
from typing import Optional

class Solution:

    def is_letter(self, chr):

        if ord(chr) - ord('a') >= 0 and ord('z') - ord(chr) >= 0:
            return True

        if ord(chr) - ord('A') >= 0 and ord('Z') - ord(chr) >= 0:
            return True

        return False

    def reverseOnlyLetters(self, s: str) -> str:
        char_arr = [c for c in s]
        l = 0
        h = len(char_arr) - 1
        while l < h:

            while l < h and not self.is_letter(char_arr[l]):
                l += 1

            while l < h and not self.is_letter(char_arr[h]):
                h -= 1

            char_arr[l], char_arr[h] = char_arr[h], char_arr[l]

            l += 1
            h -= 1

        return "".join(char_arr)


def test():
    solution = Solution()

    # test method
    print(solution.reverseOnlyLetters("ab-cd"))
    print(solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"))


test()
