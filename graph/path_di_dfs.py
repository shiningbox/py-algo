from dfs_di import DiDFS
from graph_viz import create_flight_graph, visualize_digraph
from adjacency_list_graph import Node, AdjacencyListGraph


class FindDiPathDFS(DiDFS):

    def __init__(self):
        super(FindDiPathDFS, self).__init__()
        self.path = []
        self.found = False
        self.target_v = None

    def start_visit(self, node: Node):
        self.path.append(node)
        # Only add the node on the discovery edge
        if node == self.target_v:
            self.found = True

    def end_visit(self, node: Node):
        # If all edges of vertex has been visited, and not found the node
        # Then remove the vertex
        # If found the node, then keep it
        if not self.found:
            self.path.pop()

    def execute(self, graph: AdjacencyListGraph, start: Node, data: object):
        super().execute(graph, start, data)
        self.target_v = data
        self.dfs_visit(start)
        return self.path

    def is_done(self):
        return self.found

    def print_path(self):
        result = ""
        for vertex in self.path:
            result += vertex.element() + " " + str(vertex.toplogical_index) + " > "
        result = result[:-1]
        print(result)

def simple_test():
    simple_graph = create_flight_graph()
    starting_node = simple_graph.get_vertex("BOS")
    target_node = simple_graph.get_vertex("SFO")
    search = FindDiPathDFS()
    search.execute(simple_graph, starting_node, target_node)
    search.print_path()
    visualize_digraph(simple_graph)


#simple_test()