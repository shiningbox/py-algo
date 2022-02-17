from typing import List
from typing import Optional

class Solution:

    def numSquares(self, n):
        if n < 2:
            return n
        children = []
        i = 1
        while i * i <= n:
            children.append(i * i)
            i += 1
        path_len = 0
        remains = {n}
        # each remains is a tree layer
        while remains:
            path_len += 1
            temp = set()
            for x in remains:
                for y in children:
                    # The first tree layer has zero in the remain is the shortest path
                    if x == y:
                        return path_len
                    if x < y:
                        break
                    temp.add(x - y)
            remains = temp

        return path_len



def test():
    solution = Solution()
    # test method
    print(solution.numSquares(12))
    #print(solution.numSquares(13))
    #print(solution.numSquares(41))


test()
