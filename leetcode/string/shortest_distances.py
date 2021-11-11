from typing import List
from typing import Optional

class Solution:

    def find_min_distance(self, nums, low, high, val):

        if low > high:
            return abs(val - nums[high])

        mid = (low + high) // 2

        min_dis = abs(val - nums[mid])
        left_dis = self.find_min_distance(nums, low, mid - 1, val)
        right_dis = self.find_min_distance(nums, mid + 1, high, val)

        return min(min_dis, left_dis, right_dis)


    def shortestToChar(self, s: str, c: str) -> List[int]:
        positions = []
        results = []
        index = 0
        for char in s:
            if char == c:
                positions.append(index)
            index += 1

        for i in range(len(s)):
            results.append(self.find_min_distance(positions, 0, len(positions) - 1, i))

        return results

def test():
    solution = Solution()
    # test method
    print(solution.shortestToChar("aaab", "b"))
    print(solution.shortestToChar("loveleetcode", "e"))


test()
