from typing import List
from typing import Optional

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        results = []
        start = end = 0
        while start <= len(nums) - 1:
            end = start + 1
            range_start = str(nums[start])
            range_end = None
            while end <= len(nums) - 1 and nums[end] == nums[start] + 1:
                range_end = str(nums[end])
                start = end
                end += 1
            start = end
            if not range_end:
                results.append(range_start)
            else:
                results.append(range_start + "->" + range_end)

        return results

def test():
    solution = Solution()
    # test method
    print(solution.summaryRanges([]))
    print(solution.summaryRanges([0]))
    print(solution.summaryRanges([0,1,2,4,5,7]))
    print(solution.summaryRanges([0,2,3,4,6,8,9]))


test()
