from typing import List
from typing import Optional

class Solution:
    def commonChars(self, words):
        check = list(words[0])
        for word in words[1:]:
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck
        return check


def test():
    solution = Solution()
    # test method
    print(solution.commonChars(["a"]))
    print(solution.commonChars(["bella", "label", "roller"]))
    print(solution.commonChars(["cool", "lock", "cook"]))
    print(solution.commonChars(["a", "b", "j"]))



test()
