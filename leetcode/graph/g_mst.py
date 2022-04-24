
class Kruskal_MST():

    def __init__(self):
        # Queue to save edges with weight as key
        self.queue = LinkedSortedPriorityQueue()
        self.mst = []


    def find_mst(self, graph: AdjacencyListGraph):
        # Add all edges to a priority queue
        for edge in graph.edges():
            self.queue.insert_item(edge.element(), edge)
        # Create clusters for each vertex
        for vertex in graph.vertices():
            vertex.container = set()
            vertex.container.add(vertex.element())
        # Iterate queue to add edges into mst
        while not self.queue.is_empty():
            min_edge = self.queue.remove_min_element().element
            edge_vertices = min_edge.vertices
            # If the adjacent vertices of the min edge are in different set
            # Then merge them and add min_edge to the mist
            vertex_u = edge_vertices[0]
            vertex_v = edge_vertices[1]
            if vertex_u.container != vertex_v.container:
                self.mst.append(min_edge)
                # Merge the two sets
                new_set = vertex_u.container.union(vertex_v.container)
                # Update the container for each vertex in new_set
                for v_key in new_set:
                    vertex = graph.get_vertex(v_key)
                    vertex.container = new_set
            else:
                # Otherwise, if in the same set already
                # Discard the edge
                continue


graph = create_weighted_graph()
mst = Kruskal_MST()
mst.find_mst(graph)
mst.print_mst()
