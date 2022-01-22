from typing import List
from typing import Optional

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ins = [0] * numCourses
        stack = []
        graph = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        res = []
        for edge in prerequisites:
            ins[edge[0]] += 1
            graph[edge[1]][edge[0]] = 1

        for i in range(len(ins)):
            if ins[i] == 0:
                stack.append(i)

        while stack:
            s = stack.pop(0)
            res.append(s)

            # remove s and all edges from s
            for i in range(numCourses):
                if graph[s][i] == 1:
                    graph[s][i] == 0
                    ins[i] -= 1
                    if ins[i] == 0:
                        stack.append(i)

        return len(res) == numCourses


def test():
    solution = Solution()
    # test method
    #print(solution.canFinish(7, [[2, 0], [3, 1], [4, 2], [5, 3], [5, 4], [6, 5]]))
    #print(solution.canFinish(2, [[1,0],[0,1]]))
    #print(solution.canFinish(2, [[1,0]]))
    print(solution.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))


test()
