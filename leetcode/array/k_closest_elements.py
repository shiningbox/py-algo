from typing import List
from typing import Optional

class Solution:

    min_diff = 10 ** 4
    min_idx = -1

    def binary_search(self, num, arr, l, h):
        if l > h:
            return
        mid = (l + h) // 2
        if num > arr[mid]:
            self.binary_search(num, arr, mid + 1, h)
        elif num < arr[mid]:
            self.binary_search(num, arr, l, mid - 1)

        if abs(arr[mid] - num) <= self.min_diff:
            self.min_diff = abs(arr[mid] - num)
            self.min_idx = mid

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        self.min_diff = 10 ** 4
        self.min_idx = -1
        self.binary_search(x, arr, 0, len(arr) - 1)

        res = []
        l = self.min_idx
        r = self.min_idx + 1
        count = k
        while count > 0:
            # left element is smaller
            if l >= 0 and r <= len(arr) - 1:
                if abs(arr[l] - x) < abs(arr[r] - x):
                    res.insert(0, arr[l])
                    l -= 1
                elif abs(arr[l] - x) == abs(arr[r] - x):
                    if arr[l] < arr[r]:
                        res.insert(0, arr[l])
                        l -= 1
                    else:
                        res.append(arr[r])
                        r += 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l < 0 and r <= len(arr) - 1:
                res.append(arr[r])
                r += 1
            else:
                res.insert(0, arr[l])
                l -= 1
            count -= 1
        return res


def test():
    solution = Solution()
    # test method
    print(solution.findClosestElements([1,2,3,4,5], 4, 3))
    print(solution.findClosestElements([1,2,3,4,5], 4, -1))


test()
