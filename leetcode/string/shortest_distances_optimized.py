from typing import List
from typing import Optional

class Solution:

    def shortestToChar(self, s: str, c: str) -> List[int]:
        prev = float('-inf')
        ans = []

        for i in range(len(s)):
            if s[i] == c:
                prev = i
            ans.append(i - prev)

        prev = float('inf')

        for i in range(len(s))[::-1]:
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans

def test():
    solution = Solution()
    # test method
    #print(solution.shortestToChar("aaab", "b"))
    print(solution.shortestToChar("loveleetcode", "e"))


test()
