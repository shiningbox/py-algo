from typing import List
from typing import Optional

class Solution:

    graph = {}

    def convert_edges_graph(self, edges):
        for edge in edges:
            if edge[0] in self.graph:
                self.graph[edge[0]].append(edge[1])
            else:
                self.graph[edge[0]] = [edge[1]]

    def dfs(self, v, visited, visited_e):

        # Mark the current node as visited
        # and print it
        visited.add(v)

        # Recur for all the vertices
        # adjacent to this vertex
        if v in self.graph:
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    # remove edge from edge
                    visited_e.add((v, neighbour))
                    self.dfs(neighbour, visited, visited_e)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited_v = set()
        visited_e = set()
        self.graph = {}
        v = edges[0][0]
        self.convert_edges_graph(edges)
        # Call the recursive helper function
        # to print DFS traversal
        self.dfs(v, visited_v, visited_e)

        res = None
        for edge in edges:
            if (edge[0], edge[1]) not in visited_e:
                res = edge
        print(visited_e)
        print(self.graph)
        return res

def test():
    solution = Solution()
    # test method
    print(solution.findRedundantConnection([[1,2],[1,3],[2,3]]))
    #print(solution.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))


test()
