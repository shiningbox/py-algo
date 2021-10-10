from typing import List
from typing import Optional


class Solution(object):
    def intersect(self, nums1, nums2):
        n1, n2, res = sorted(nums1), sorted(nums2), []
        p1 = p2 = 0
        while p1 < len(n1) and p2 < len(n2):
            if n1[p1] < n2[p2]:
                p1 += 1
            elif n2[p2] < n1[p1]:
                p2 += 1
            else:
                res.append(n1[p1])
                p1 += 1
                p2 += 1
        return res


def test():
    solution = Solution()
    # test method
    print(solution.intersect([1, 2, 2, 1], [2, 2]))
    print(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print(solution.intersect([1], [0]))
    print(solution.intersect([1], [1]))
    print(solution.intersect([1, 2], [1, 1]))
    print(solution.intersect([1, 2], [1, 2]))
    print(solution.intersect([1, 2], [1, 1, 1]))
    print(solution.intersect([1, 2, 2, 1], [1, 1]))
    print(solution.intersect([8, 0, 3], [0, 0]))


test()
