from typing import List
from typing import Optional

class Solution:
    def countSubstrings(self, s: str) -> int:
        lens = len(s)
        matrix = [[0 for i in range(lens)] for j in range(lens)]
        count = 0
        for end in range(lens):
            for start in range(0, end + 1):
                if start == end:
                    matrix[end][start] = 1
                    count += 1
                elif end - start == 1:
                    if s[start] == s[end]:
                        matrix[end][start] = 1
                        count += 1
                else:
                    # check if from end - 1 to start + 1 is palindrome
                    # if yes, then check if s[start] == s[end]
                    if matrix[end - 1][start + 1] == 1 and s[start] == s[end]:
                        matrix[end][start] = 1
                        count += 1

        return count


def test():
    solution = Solution()
    # test method
    # print(solution.method("test"))


test()
