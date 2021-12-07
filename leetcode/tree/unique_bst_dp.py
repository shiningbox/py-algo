from typing import List
from typing import Optional

class Solution:
    """We can also solve it using iterative dynamic programming. Again, the logic is similar to above
    with slight change in approach that we start from base conditions instead of other way around.
    We have base conditions of dp[0] = dp[1] = 1.
    Then we calculate result for each number of nodes i from 2...n one after another.
    For i nodes. we can consider each of the node j from 1...i as the root node of BST.
    Considering the jth node as the root node in BST having total of i nodes, the final result is
    summation of dp[j-1] * dp[i-j], for all j from 1...i. (Comparing to above solution
    dp[j-1] = numTrees(j-1) and dp[i-j]=numTrees(i-j))"""
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]


def test():
    solution = Solution()
    # test method
    print(solution.numTrees(3))
    print(solution.numTrees(1))
    print(solution.numTrees(5))


test()
