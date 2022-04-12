

class Node:

    def __init__(self, type, data):
        self.type = type
        self.data = data


class Graph:

    def __init__(self):
        self.nodes = []
        self.edges = []

    def print_graph(self):
        for edge in self.edges:
            print(f"{edge[0].type} {edge[0].data} is connected with {edge[1].type} {edge[1].data}")

    def get_provider_degree(self, id: str) -> int:
        degree = 0
        for edge in self.edges:
            if edge[0].type == 'customer' and edge[1].type == 'provider' and edge[1].data == id:
                degree += 1

        return degree


customer1 = Node("customer", "001")
customer2 = Node("customer", "002")
customer3 = Node("customer", "003")

prov1 = Node("provider", "001")
prov2 = Node("provider", "002")

doc1 = Node("doctor", "001")

# Create graph
graph = Graph()

# Create edges
edge1 = (customer1, prov1)
edge2 = (customer2, prov1)
edge3 = (customer3, prov2)
edge4 = (customer3, prov1)
edge5 = (prov1, doc1)
edge6 = (customer1, doc1)

graph.edges.append(edge1)
graph.edges.append(edge2)
graph.edges.append(edge3)
graph.edges.append(edge4)
graph.edges.append(edge5)
graph.edges.append(edge6)

graph.print_graph()

print(graph.get_provider_degree("001"))


