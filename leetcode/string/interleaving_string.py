from typing import List
from typing import Optional

class Solution:

    def isInterleave(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        dp = [[True for _ in range(c + 1)] for _ in range(r + 1)]
        for i in range(1, r + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, c + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
        print(dp)
        return dp[-1][-1]


def test():
    solution = Solution()
    # test method
    print(solution.isInterleave("aabc", "bdd", "aabdbcd"))
    #print(solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    #print(solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))


test()
