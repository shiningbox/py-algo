from typing import List
from typing import Optional

class Solution:

    def cicular_travel(self, current, gas, tank, cost):

        start = current
        tank = tank + gas[current] - cost[current]
        next = (start + 1) % len(gas)
        reached = -1
        # Can go next
        while tank >= 0:
            if next == start:
                reached = start
                break
            current = next
            next = (next + 1) % len(gas)
            tank = tank + gas[current] - cost[current]

        return reached

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx_dict = {}
        idx = 0
        for num in gas:
            if num not in idx_dict:
                idx_dict[num] = [idx]
            else:
                idx_dict[num].append(idx)
            idx += 1

        gas_sorted = list(gas)
        gas_sorted.sort()
        for i in range(len(gas_sorted) - 1, -1, -1):
            res = self.cicular_travel(idx_dict[gas_sorted[i]].pop(), gas, 0, cost)
            if res != -1:
                return res
        return -1


def test():
    solution = Solution()
    # test method
    print(solution.canCompleteCircuit([1, 2, 3,4,5], [3,4,5,1,2]))
    print(solution.canCompleteCircuit([2,3,4], [3,4,3]))
    print(solution.canCompleteCircuit([4,5,3,1,4], [5,4,3,4,2]))
    print(solution.canCompleteCircuit([2,0,1,2,3,4,0], [0,1,0,0,0,0,11]))


test()
