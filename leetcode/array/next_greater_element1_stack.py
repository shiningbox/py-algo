from typing import List
from typing import Optional


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_map = {x: -1 for x in nums1}
        # a stack to keep nums less than current num
        # then add the current num
        stack = []

        # if top less than num
        # add an dict entry with d[top] = num
        for num in nums2:
            while stack and num > stack[-1]:
                top_num = stack.pop()
                if top_num in greater_map:
                    greater_map[top_num] = num
            stack.append(num)

        return [greater_map[x] for x in nums1]


def test():
    solution = Solution()
    # test method
    print(solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2, 5]))
    print(solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    print(solution.nextGreaterElement([2, 4], [1, 2, 3, 4]))


test()
