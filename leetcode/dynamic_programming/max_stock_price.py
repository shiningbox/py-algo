from typing import List
from typing import Optional

class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        profit = [0] * len(prices)
        min_price = 0
        max_profit = 0
        for i in range(1, len(prices)):
            # If current price is less than min before i
            # Then current price can not bring any profit
            if prices[i] <= min_price:
                min_price = prices[i]
                continue
            # Calculate the current profit
            current_profit = prices[i] - min_price
            # Compare with the previous profit
            profit[i] = max(profit[i - 1], current_profit)
            if profit[i] >= max_profit:
                max_profit = profit[i]

        return max_profit

    def maxProfit_slow(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        profit = [0] * len(prices)
        mins = [0] * len(prices)
        mins[0] = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            current_profit = 0
            j = 0
            # If current price is less than min before i
            # Then current price can not bring any profit
            if prices[i] <= mins[i - 1]:
                mins[i] = prices[i]
                continue
            else:
                mins[i] = mins[i - 1]
            # Calculate the current profit
            while j < i:
                if prices[i] - prices[j] >= current_profit:
                    current_profit = prices[i] - prices[j]
                j += 1
            # Compare with the previous profit
            profit[i] = max(profit[i - 1], current_profit)
            if profit[i] >= max_profit:
                max_profit = profit[i]

        return max_profit

def test():
    solution = Solution()
    # test method
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit([7, 6, 4, 3, 1]))


test()
