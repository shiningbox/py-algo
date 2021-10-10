from typing import List
from typing import Optional

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        nums = []
        c = s + t
        for char in c:
            nums.append(ord(char))

        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]

        return chr(res)


def test():
    solution = Solution()
    # test method
    print(solution.findTheDifference("abcd", "abcde"))
    print(solution.findTheDifference("", "y"))
    print(solution.findTheDifference("a", "aa"))
    print(solution.findTheDifference("ae", "aea"))


test()
