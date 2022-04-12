from dfs import DFS
from graph_viz import create_simple_graph, visualize_ungraph
from adjacency_list_graph import Node, AdjacencyListGraph


class FindCycleDFS(DFS):

    def __init__(self):
        super(FindCycleDFS, self).__init__()
        self.cycle_start_v = None
        self.path = []
        self.cycle = []
        self.found = False

    def start_visit(self, node: Node):
        # Add the current visiting node to path
        self.path.insert(0, node)

    def end_visit(self, node: Node):
        # If all edges of vertex has been visited, and not found cycle
        # Then remove the vertex
        # If found a cycle, then keep it
        if not self.found:
            self.path.remove(self.path[0])

    def execute(self, graph: AdjacencyListGraph, start: Node, data: object):
        super().execute(graph, start, data)
        self.dfs_visit(start)
        for vertex in self.path:
            self.cycle.append(vertex)
            if vertex == self.cycle_start_v:
                break
        return self.cycle

    def is_done(self):
        return self.found

    def print_cycle(self):
        result = ""
        for vertex in self.cycle:
            result += vertex.element() + ">"
        result = result[:-1]
        print(result)

    def print_path(self):
        result = ""
        for vertex in self.path:
            result += vertex.element() + ">"
        result = result[:-1]
        print(result)

    def traverse_back(self, edge: Node, vertex: Node):
        e_key = edge.element()
        v_key = vertex.element()
        # Find the cycle start node
        self.cycle_start_v = self.graph.opposite(v_key, e_key)
        print(self.cycle_start_v.element())
        self.found = True

def simple_test():
    simple_graph = create_simple_graph()
    starting_node = simple_graph.get_vertex("K")
    search = FindCycleDFS()
    search.execute(simple_graph, starting_node, None)
    search.print_path()
    search.print_cycle()
    visualize_ungraph(simple_graph)

simple_test()