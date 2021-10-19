from typing import List
from typing import Optional


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        sum = duration
        current = timeSeries[0]
        updated_duration = duration
        for i in range(1, len(timeSeries)):
            next = timeSeries[i]
            if next - current >= updated_duration:
                sum += updated_duration
                current = next
                updated_duration = duration
            else:
                sum += next - current
                current = next
                updated_duration = duration - (next - current)

        return sum

def test():
    solution = Solution()
    # test method
    print(solution.findPoisonedDuration([1, 4], 2))
    print(solution.findPoisonedDuration([1, 2], 2))
    print(solution.findPoisonedDuration([1], 2))
    print(solution.findPoisonedDuration([1,3,5,7,9,11,13,15], 3))


test()
