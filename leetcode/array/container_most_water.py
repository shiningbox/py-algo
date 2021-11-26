from typing import List
from typing import Optional


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:

            if height[i] >= height[j]:
                shorter = j
            else:
                shorter = i

            area = (j - i) * height[shorter]
            print(i, j, area)

            if area >= max_area:
                max_area = area

            if shorter == j:
                next = j - 1
                while next >= i:
                    if height[next] >= height[shorter]:
                        break
                    next -= 1
                j = next
            else:
                next = i + 1
                while next <= j:
                    if height[next] >= height[shorter]:
                        break
                    next += 1
                i = next

        return max_area

def test():
    solution = Solution()
    # test method
    print(solution.maxArea([1,2,4,3]))
    #print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
    #print(solution.maxArea([9,8,6,2,5,4,8,3,9]))
    #print(solution.maxArea([4,3,2,1,4]))
    #print(solution.maxArea([1, 2, 1]))
    #print(solution.maxArea([1, 1]))
    #print(solution.maxArea([1,3,2,5,25,24,5]))
    #print(solution.maxArea([1,8,100,2,100,4,8,3,7]))
    #print(solution.maxArea([75,21,3,152,13,107,163,166,32,160,41,131,7,67,56,5,153,176,29,139,61,149,176,142,64,75,170,156,73,48,148,101,70,103,53,83,11,168,1,195,81,43,126,88,62,134,45,167,63,26,107,124,128,83,67,192,158,189,149,184,37,49,85,107,152,90,143,115,58,
    #                        144,62,139,139,189,180,153,75,177,121,138,4,28,15,132,63,82,124,174,23,25,110,60,74,147,120,179,37,63,94,47]))


test()
