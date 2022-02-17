from typing import List
from typing import Optional

class Solution:


    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        coins.sort(reverse=True)

        lefts = [amount]
        visited = [False] * (amount + 1)
        visited[0] = True
        path_len = 0

        while lefts:
            path_len += 1
            temp = set()
            for left in lefts:
                for coin in coins:
                    if left - coin == 0:
                        return path_len
                    elif left > coin:
                        if not visited[left - coin]:
                            visited[left - coin] = True
                            temp.add(left - coin)
            lefts = temp

        return -1

def test():
    solution = Solution()
    # test method
    print(solution.coinChange([1,2,5], 11))
    print(solution.coinChange([2,4,6,8,10,12,14,16,18,20,22,24], 9999))
    print(solution.coinChange([1], 0))


test()
