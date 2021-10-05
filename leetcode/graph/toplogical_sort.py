from list.array_queue import ArrayQueue
from path_di_dfs import FindDiPathDFS
from graph_viz import create_dag, visualize_digraph
from adjacency_list_graph import AdjacencyListGraph


class ToplogicalSort():

    def __init__(self, graph: AdjacencyListGraph):
        self.graph = graph
        self.queue = ArrayQueue(100)

    def sort(self):
        # Find vertex with incoming degree to be zero
        # and insert them into a queue
        for vertex in self.graph.vertices():
            if vertex.num_incoming_edges == 0:
                self.queue.enqueue(vertex)
        toplogical_index = 1
        while not self.queue.is_empty():
            current_vertex = self.queue.dequeue()
            current_vertex.toplogical_index = toplogical_index
            vertex_key = current_vertex.element()
            # Processed current vertex, increase the toplogical index by 1
            toplogical_index += 1
            for edge in self.graph.out_incident_edges(vertex_key):
                edge_key = edge.element()
                opposite_vertex = self.graph.opposite(vertex_key, edge_key)
                # Reduce incoming adjacent vertices of current_vertex by 1
                opposite_vertex.num_incoming_edges -= 1
                # If this vertex has no incoming vertex, then enqueue
                if opposite_vertex.num_incoming_edges == 0:
                    self.queue.enqueue(opposite_vertex)


def simple_testing():
    dag = create_dag()
    starting_node = dag.get_vertex("B")
    target_node = dag.get_vertex("H")
    search = FindDiPathDFS()
    search.execute(dag, starting_node, target_node)
    top_sort = ToplogicalSort(dag)
    top_sort.sort()
    search.print_path()
    visualize_digraph(dag)


simple_testing()
