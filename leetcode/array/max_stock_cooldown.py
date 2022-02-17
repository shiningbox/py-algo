from typing import List
from typing import Optional


class Solution:

    # Then the second day
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        # Define three states:
        # S0: Read to buy state (won't generate profit from current state)
        # S1: Bought, ready to sell state (won't generate profit from current state)
        # S2: Cooldown state (may generate profit from current state due to sell action)
        s0 = [0] * len(prices)
        s1 = [0] * len(prices)
        s2 = [0] * len(prices)

        # S0 -rest-> S0
        # S0 -buy-> S1
        # S1 -rest-> S1
        # S1 -sell-> S2
        # S2 -rest-> S0

        # Si[j]: the profit at jth day ended with i state
        # Given initial state, the initial profit:
        # S0[0]: 0 (not buying)
        # S1[0]: -price[0] (buy the stock at first day's price)
        # S2[0]: -inf (can not sell at the first day)

        s0[0] = 0
        s1[0] = -1 * prices[0]
        s2[0] = float('-inf')

        # Then for day i,
        # if state is S0, either come from itself S0[i-1] (rest from ready to buy) or S2[i-1] (rest from Cooldown)
        # S0[i] = max(S0[i], S2[i-1])
        # if state is S1, either come from itself S1[i-1] (rest from ready to sell) or S0[i-1] (rest from Cooldown)
        # S1[i] = max(S1[i-1], S0[i-1] - prices[i])
        # If state is S2, could only come from S1
        # S2[i] = S1[i - 1] + prices[i]

        for i in range(1, len(prices)):
            s0[i] = max(s0[i-1], s2[i - 1])
            s1[i] = max(s1[i-1], (s0[i-1] - prices[i]))
            s2[i] = s1[i - 1] + prices[i]

        return max(s0[-1], s2[-1])


def test():
    solution = Solution()
    # test method
    print(solution.maxProfit([1,2,3,0,2]))
    print(solution.maxProfit([1,2,4]))

test()
