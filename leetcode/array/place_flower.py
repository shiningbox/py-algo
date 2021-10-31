from typing import List
from typing import Optional

class Solution:

    def check_left(self, nums, i):
        if i - 1 < 0:
            return True
        else:
            if nums[i - 1] == 1:
                return False
            else:
                return True

    def check_right(self, nums, i):
        if i + 1 > len(nums) - 1:
            return True
        else:
            if nums[i + 1] == 1:
                return False
            else:
                return True

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = count = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if self.check_left(flowerbed, i) and self.check_right(flowerbed, i):
                    count += 1
                    flowerbed[i] = 1
            if i + 2 > len(flowerbed) - 1:
                i += 1
            else:
                i += 2
        return count >= n


def test():
    solution = Solution()
    # test method
    print(solution.canPlaceFlowers([1,0,0,0,1], 1))
    print(solution.canPlaceFlowers([1,0,0,0,1], 2))
    print(solution.canPlaceFlowers([0,0,0,0,0], 2))
    print(solution.canPlaceFlowers([0], 1))
    print(solution.canPlaceFlowers([1], 1))
    print(solution.canPlaceFlowers([0,1,0,1,0,1,0,0], 1))
    print(solution.canPlaceFlowers([0, 0], 2))


test()
