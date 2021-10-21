from typing import List
from typing import Optional

class Solution:
    def find_modes(self, nums):
        prev = None
        c_count = 0
        m_count = 0
        results = []
        for num in nums:
            if num != prev:
                c_count = 1
            else:
                c_count += 1
            # if c_count, the count of current num equals max count
            # add the current num as well
            if c_count == m_count:
                results.append(num)
            # if c_count of this num is larger than max count
            # then only need to add this num
            elif c_count > m_count:
                results = [num]
                m_count = c_count
            prev = num
        return results


def test():
    solution = Solution()
    # test method
    print(solution.find_modes([2, 3, 3, 3, 4, 4, 5]))
    print(solution.find_modes([2, 3, 3, 3, 4, 4, 4]))
    print(solution.find_modes([2, 3, 5]))
    print(solution.find_modes([2]))


test()
