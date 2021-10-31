from typing import List
from typing import Optional

class Solution:

    def findMaxAverage(self, A, K):
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        ma = max(P[i + K] - P[i]
                 for i in range(len(A) - K + 1))
        return ma / float(K)

    def findMaxAverage_sliding_window(self, nums: List[int], k: int) -> float:
        i = 0
        max_avg = -10 ** 4
        while i <= len(nums) - k:
            sum = 0
            for j in range(i, i + k):
                print(nums[j])
                sum += nums[j]
            avg = sum / k
            if avg >= max_avg:
                max_avg = avg
            i += 1
        return max_avg


def test():
    solution = Solution()
    # test method
    print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
    print(solution.findMaxAverage([5], 1))


test()
