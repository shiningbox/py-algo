from typing import List
from typing import Optional

class Solution:

    """

        Suppose from cur -> i - 1, with some positive tank (can not be negative), meaning can go from res to i - 1 with
        some more gas

        If i makes tank negative, gas[i] is less than cost[i], and diff is bigger than tank

        Since each tank between cur and i-1 is positive, subtracting any accumulation from res to j
        (an index between res to i-1) will make diff bigger than the accumulation even more,
        thus definitely negative to start from any j, between res and i-1

        i also can not be selected because its gas[i] < cost[i]

        Then the only next position is from i + 1

    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        res = 0
        total_accum = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            # Then start from i + 1 because any place from res to i can not be selected (hit an negative)
            if tank < 0:
                total_accum += tank
                tank = 0
                res = i + 1
        total_accum += tank
        return -1 if total_accum < 0 else res

def test():
    solution = Solution()
    # test method
    print(solution.canCompleteCircuit([1, 2, 3,4,5], [3,4,5,1,2]))
    print(solution.canCompleteCircuit([2,3,4], [3,4,3]))
    print(solution.canCompleteCircuit([4,5,3,1,4], [5,4,3,4,2]))
    print(solution.canCompleteCircuit([2,0,1,2,3,4,0], [0,1,0,0,0,0,11]))


test()
