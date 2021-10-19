from typing import List
from typing import Optional

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        sum = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                sum += 1
                i += 1
                j += 1
                continue
            j += 1

        return sum

def test():
    solution = Solution()
    # test method
    print(solution.findContentChildren([1, 2, 3], [1, 1]))
    print(solution.findContentChildren([1, 2], [1, 2, 3]))
    print(solution.findContentChildren([1], []))
    print(solution.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))


test()
