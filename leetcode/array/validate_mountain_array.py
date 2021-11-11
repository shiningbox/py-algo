from typing import List
from typing import Optional

class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:
        status = -2
        increase = 0
        decrease = 0
        i = 0
        j = 1
        while j < len(arr):

            if arr[i] == arr[j]:
                return False
            # decrease
            elif arr[i] > arr[j]:
                if status == -2:
                    return False
                elif status == 1:
                    status = -1
                    decrease += 1
            # increase
            else:
                if status == -2:
                    status = 1
                    increase += 1
                elif status == -1:
                    status = 1
                    increase += 1
            i = j
            j += 1
        return increase == 1 and decrease == 1

def test():
    solution = Solution()
    # test method
    print(solution.validMountainArray([2, 1]))
    print(solution.validMountainArray([3,5,5]))
    print(solution.validMountainArray([0,3,2,1]))
    print(solution.validMountainArray([2,1,2,3,5,7,9,10,12,14,15,16,18,14,13]))
    print(solution.validMountainArray([2,0,2]))


test()
