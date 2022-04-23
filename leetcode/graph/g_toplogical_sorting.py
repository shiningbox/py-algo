from typing import List
from typing import Optional


def canFinish(prerequisites: List[List[int]]) -> bool:
    ins = 0
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

