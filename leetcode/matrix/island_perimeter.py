from typing import List
from typing import Optional

class Solution:

    def get_adjacents(self, grid, i, j):
        rows = len(grid)
        cols = len(grid[0])
        adjacents = []
        # left
        if j - 1 >= 0 and grid[i][j-1] == 1:
            adjacents.append((i, j-1))
        # right
        if j + 1 < cols and grid[i][j+1] == 1:
            adjacents.append((i, j+1))
        # top
        if i - 1 >= 0 and grid[i-1][j] == 1:
            adjacents.append((i-1, j))
        # bottom
        if i + 1 < rows and grid[i+1][j] == 1:
                adjacents.append((i+1, j))
        return adjacents


    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # BFS with queue
        visited_queue = []
        visited_dict = {}
        # Find initial point
        stop = False
        s_i = 0
        s_j = 0
        for i in range(len(grid)):
            if stop:
                break
            col = grid[i]
            for j in range(len(col)):
                if grid[i][j] == 1:
                    stop = True
                    s_i = i
                    s_j = j
                    break
        visited_queue.append((s_i, s_j))
        perimeter = 0
        while visited_queue:
            # BFS
            head = visited_queue.pop(0)
            if str(head[0]) + str(head[1]) not in visited_dict:
                visited_dict[str(head[0]) + str(head[1])] = 1
            else:
                continue
            adjacents = self.get_adjacents(grid, head[0], head[1])
            adj_size = len(adjacents)
            perimeter += 4 - adj_size
            for node in adjacents:
                if str(node[0]) + str(node[1]) not in visited_dict:
                    visited_queue.append(node)

        return perimeter

def test():
    solution = Solution()
    # test method
    print(solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(solution.islandPerimeter([[1]]))
    print(solution.islandPerimeter([[1,0]]))
    print(solution.islandPerimeter([[1,1],[1,1]]))


test()
