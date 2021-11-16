from typing import List
from typing import Optional


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dest_dict = {}
        source_dict = {}
        for pair in trust:
            source = pair[0]
            dest = pair[1]

            if dest not in dest_dict:
                dest_dict[dest] = 1
            else:
                dest_dict[dest] += 1

            if source not in source_dict:
                source_dict[source] = 1
            else:
                source_dict[source] += 1

        if not dest_dict and not source_dict and n == 1:
            return 1

        candidates = []
        for key, val in dest_dict.items():
            if val == n - 1 and key not in source_dict:
                candidates.append(key)

        if len(candidates) == 1:
            return candidates[0]
        else:
            return -1

def test():
    solution = Solution()
    # test method
    print(solution.findJudge(2, [[1, 2]]))
    print(solution.findJudge(3, [[1, 3], [2, 3]]))
    print(solution.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
    print(solution.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))

test()
