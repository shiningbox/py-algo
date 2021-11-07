from typing import List
from typing import Optional

class Solution:

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew_dicts = {}
        for jew in jewels:
            if jew not in jew_dicts:
                jew_dicts[jew] = jew

        count = 0
        for stone in stones:
            if stone in jew_dicts:
                count += 1

        return count


def test():
    solution = Solution()
    # test method
    print(solution.numJewelsInStones("aA", "aAAbbbb"))
    print(solution.numJewelsInStones("z", "ZZ"))


test()
