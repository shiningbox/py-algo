from typing import List
from typing import Optional

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c_low = ord('A')
        c_high = ord('Z')
        first_cap = True
        rest_cap = True
        rest_lower = True
        for i in range(len(word)):
            if i == 0:
                if ord(word[i]) > c_high or ord(word[i]) < c_low:
                    first_cap = False
            else:
                if ord(word[i]) < c_low or ord(word[i]) > c_high:
                    rest_cap = False
                else:
                    rest_lower = False

        if first_cap:
            return rest_cap or rest_lower
        else:
            return rest_lower


def test():
    solution = Solution()
    # test method
    print(solution.detectCapitalUse("test"))
    print(solution.detectCapitalUse("USA"))
    print(solution.detectCapitalUse("FlaG"))
    print(solution.detectCapitalUse("Flag"))


test()
