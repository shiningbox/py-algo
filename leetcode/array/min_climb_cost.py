from typing import List
from typing import Optional

class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        min_cost = [0] * (len(cost) + 2)
        for i in range(2, len(min_cost)):
            c_i = i - 2
            min_cost[i] = min(cost[c_i] + min_cost[i-1], cost[c_i] + min_cost[i-2])
        return min_cost[-1]

def test():
    solution = Solution()
    # test method
    print(solution.minCostClimbingStairs([10,15,20]))
    print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))


test()
