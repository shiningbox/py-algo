from list.array_queue import ArrayQueue
from priority_queue.unsorted_priority_queue import UnsortedPriorityQueue
from graph_viz import create_weighted_graph, visualize_ungraph
from adjacency_list_graph import AdjacencyListGraph, Node


class Dijkstra():

    def __init__(self):
        # The priority queue to contain nodes to be calculated shortest distance
        self.queue = UnsortedPriorityQueue()

    def print_queue(self):
        if not self.queue.is_empty():
            current_node = self.queue.header.next
            while True:
                print(f"Key is: {current_node.element.key}, Element is: {current_node.element.element.element()}")
                current_node = current_node.next
                if current_node == self.queue.tail:
                    break
        else:
            print("Empty Sequence")

    def print_vertices(self, graph):
        for vertex in graph.vertices():
            print(f"{vertex.element()},  {vertex.distance}")

    def find_shortest_path(self, graph: AdjacencyListGraph, v: Node):
        # Initialize the queue with node and distances
        for vertex in graph.vertices():
            if vertex == v:
                vertex.distance = 0
            else:
                vertex.distance = float('inf')
            self.queue.insert_item(vertex.distance, vertex)
        while not self.queue.is_empty():
            # Starting with the node with minimal distances
            current_v = self.queue.remove_min_element().element
            vertex_key = current_v.element()
            # Find its adjacent vertices
            for adj_e in graph.adjacent_edges(vertex_key):
                edge_key = adj_e.element()
                opp_v = graph.opposite(vertex_key, edge_key)
                # Check if its adjacent vertices's distance needs to be updated
                # d(opp_v) = adj_e.weight + d(current_v)
                if current_v.distance + adj_e.weight <= opp_v.distance:

                    opp_v.distance = current_v.distance + adj_e.weight

        self.print_vertices(graph)


flight_di_graph = create_weighted_graph()
dijkstra = Dijkstra()
starting_node = flight_di_graph.get_vertex("BWI")
dijkstra.find_shortest_path(flight_di_graph, starting_node)
visualize_ungraph(flight_di_graph, draw_edge=True)
