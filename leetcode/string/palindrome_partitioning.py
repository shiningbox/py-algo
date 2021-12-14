from typing import List
from typing import Optional

class Solution:

    def check_palindrome(self, s):

        if len(s) <= 1:
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def sub_partition(self, sub, path, res):

        if len(sub) == 0:
            res.append(path)

        for i in range(len(sub)):
            prefix = sub[0:i + 1]

            if self.check_palindrome(prefix):
                self.sub_partition(sub[i+1:], path + [prefix], res)

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.sub_partition(s, [], res)
        return res


def test():
    solution = Solution()
    # test method
    print(solution.partition("aab"))


test()

