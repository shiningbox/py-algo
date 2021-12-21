from typing import List
from typing import Optional


class Solution:

    def cicular_travel(self, current, gas, tank, cost):

        start = current
        tank = tank + gas[current] - cost[current]
        next = (start + 1) % len(gas)
        reached = -1
        # Tank left if goes to next station
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
        diff = []
        zip_object = zip(gas, cost)

        for list1_i, list2_i in zip_object:
            diff.append(list1_i - list2_i)

        for num in diff:
            if num not in idx_dict:
                idx_dict[num] = [idx]
            else:
                idx_dict[num].append(idx)
            idx += 1

        cost_sorted = list(diff)
        cost_sorted.sort()
        for i in range(len(cost_sorted) - 1, -1, -1):
            res = self.cicular_travel(idx_dict[cost_sorted[i]].pop(), gas, 0, cost)
            if res != -1:
                return res
        return -1


def test():
    solution = Solution()
    # test method
    print(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
    print(solution.canCompleteCircuit([4, 5, 3, 1, 4], [5, 4, 3, 4, 2]))
    print(solution.canCompleteCircuit([2, 0, 1, 2, 3, 4, 0], [0, 1, 0, 0, 0, 0, 11]))


test()
