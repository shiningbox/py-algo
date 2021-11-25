from typing import List
from typing import Optional

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res_dict = {}
        revert_dict = {}
        for num in arr:
            if num not in res_dict:
                res_dict[num] = 1
            else:
                res_dict[num] += 1
        for key, value in res_dict.items():
            if value not in revert_dict:
                revert_dict[value] = value
            else:
                return False
        return True

def test():
    solution = Solution()
    # test method
    print(solution.uniqueOccurrences([1,2,2,1,1,3]))
    print(solution.uniqueOccurrences([1,2]))


test()
