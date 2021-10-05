import matplotlib.pyplot as plt
import networkx as nx
from adjacency_list_graph import AdjacencyListGraph


def create_simple_graph():
    graph = AdjacencyListGraph()
    graph.insert_vertex("A")
    graph.insert_vertex("B")
    graph.insert_vertex("C")
    graph.insert_vertex("D")
    graph.insert_vertex("E")
    graph.insert_vertex("F")
    graph.insert_vertex("G")
    graph.insert_vertex("H")
    graph.insert_vertex("I")
    graph.insert_vertex("J")
    graph.insert_vertex("K")
    graph.insert_vertex("L")
    graph.insert_vertex("M")
    graph.insert_vertex("N")
    graph.insert_vertex("O")
    graph.insert_vertex("P")
    graph.insert_vertex("Z")
    graph.insert_vertex("Y")

    graph.insert_edge("A", "B", "AB")
    graph.insert_edge("A", "E", "AE")
    graph.insert_edge("A", "F", "AF")
    graph.insert_edge("E", "F", "EF")
    graph.insert_edge("B", "F", "BF")
    graph.insert_edge("B", "C", "BC")
    graph.insert_edge("C", "G", "CG")
    graph.insert_edge("C", "D", "CD")
    graph.insert_edge("D", "G", "DG")
    graph.insert_edge("D", "H", "DH")
    graph.insert_edge("E", "I", "EI")
    graph.insert_edge("F", "I", "FI")
    graph.insert_edge("I", "M", "IM")
    graph.insert_edge("I", "N", "IN")
    graph.insert_edge("I", "J", "IJ")
    graph.insert_edge("M", "N", "MN")

    graph.insert_edge("J", "K", "JK")
    graph.insert_edge("J", "G", "JG")
    graph.insert_edge("N", "K", "NK")
    graph.insert_edge("G", "K", "GK")
    graph.insert_edge("G", "L", "GL")
    graph.insert_edge("K", "O", "KO")
    graph.insert_edge("O", "P", "OP")
    graph.insert_edge("L", "P", "LP")
    graph.insert_edge("H", "L", "HL")

    return graph


def create_dag():
    graph = AdjacencyListGraph()
    graph.insert_vertex("A")
    graph.insert_vertex("B")
    graph.insert_vertex("C")
    graph.insert_vertex("D")
    graph.insert_vertex("E")
    graph.insert_vertex("F")
    graph.insert_vertex("G")
    graph.insert_vertex("H")

    graph.insert_edge("A", "C", "AC")
    graph.insert_edge("A", "D", "AD")
    graph.insert_edge("B", "D", "BD")
    graph.insert_edge("B", "F", "BF")
    graph.insert_edge("C", "E", "CE")
    graph.insert_edge("C", "D", "CD")
    graph.insert_edge("D", "F", "DF")
    graph.insert_edge("E", "G", "EG")
    graph.insert_edge("F", "G", "FG")
    graph.insert_edge("G", "H", "GH")

    return graph


def create_flight_graph():
    graph = AdjacencyListGraph()
    graph.insert_vertex("BOS")
    graph.insert_vertex("JFK")
    graph.insert_vertex("MIA")
    graph.insert_vertex("DFW")
    graph.insert_vertex("LAX")
    graph.insert_vertex("ORD")
    graph.insert_vertex("SFO")

    graph.insert_edge("BOS", "JFK", "NW 35")
    graph.insert_edge("BOS", "MIA", "DL 247")
    graph.insert_edge("JFK", "MIA", "AA 903")
    graph.insert_edge("JFK", "DFW", "AA 1387")
    graph.insert_edge("JFK", "SFO", "TW 45")
    graph.insert_edge("MIA", "DFW", "AA 523")
    graph.insert_edge("MIA", "LAX", "AA 411")
    graph.insert_edge("DFW", "LAX", "AA 49")
    graph.insert_edge("DFW", "ORD", "DL 335")
    graph.insert_edge("ORD", "DFW", "UA 877")
    graph.insert_edge("LAX", "ORD", "UA 120")

    return graph


def create_weighted_graph():
    graph = AdjacencyListGraph()
    graph.insert_vertex("BOS")
    graph.insert_vertex("PVD")
    graph.insert_vertex("ORD")
    graph.insert_vertex("JFK")
    graph.insert_vertex("BWI")
    graph.insert_vertex("MIA")
    graph.insert_vertex("DFW")
    graph.insert_vertex("LAX")
    graph.insert_vertex("SFO")

    graph.insert_edge("BOS", "JFK", 187)
    graph.insert_edge("BOS", "ORD", 867)
    graph.insert_edge("BOS", "SFO", 2704)
    graph.insert_edge("BOS", "MIA", 1258)
    graph.insert_edge("PVD", "ORD", 849)
    graph.insert_edge("PVD", "JFK", 144)
    graph.insert_edge("ORD", "SFO", 1846)
    graph.insert_edge("ORD", "DFW", 802)
    graph.insert_edge("ORD", "JFK", 740)
    graph.insert_edge("ORD", "BWI", 621)
    graph.insert_edge("JFK", "MIA", 1090)
    graph.insert_edge("JFK", "BWI", 184)
    graph.insert_edge("BWI", "MIA", 946)
    graph.insert_edge("DFW", "SFO", 1464)
    graph.insert_edge("DFW", "LAX", 1235)
    graph.insert_edge("DFW", "MIA", 1121)
    graph.insert_edge("DFW", "JFK", 1391)
    graph.insert_edge("LAX", "SFO", 337)
    graph.insert_edge("LAX", "MIA", 2342)

    return graph

def test_flight_graph():
    graph = AdjacencyListGraph()
    graph.insert_vertex("BOS")
    graph.insert_vertex("JFK")
    graph.insert_vertex("MIA")
    graph.insert_vertex("DFW")
    graph.insert_vertex("LAX")
    graph.insert_vertex("ORD")
    graph.insert_vertex("SFO")

    graph.insert_edge("BOS", "JFK", "NW 35")
    graph.insert_edge("BOS", "MIA", "DL 247")
    graph.insert_edge("JFK", "MIA", "AA 903")
    graph.insert_edge("JFK", "DFW", "AA 1387")
    graph.insert_edge("JFK", "SFO", "TW 45")
    graph.insert_edge("MIA", "DFW", "AA 523")
    graph.insert_edge("MIA", "LAX", "AA 411")
    graph.insert_edge("DFW", "LAX", "AA 49")
    graph.insert_edge("DFW", "ORD", "DL 335")
    graph.insert_edge("ORD", "DFW", "UA 877")
    graph.insert_edge("LAX", "ORD", "UA 120")

    print("SFO degrees: ")
    print(graph.in_degree("SFO"))
    for edge in graph.in_incident_edges("SFO"):
        print(edge.element())
    for edge in graph.out_incident_edges("SFO"):
        print(edge.element())

    print("ORD degrees: ")
    print(graph.in_degree("ORD"))
    print(graph.degree("ORD"))
    print("---")
    for edge in graph.in_incident_edges("ORD"):
        print(edge.element())
    for vertex in graph.in_adjacent_vertices("ORD"):
        print(vertex.element())
    print("---")
    for vertex in graph.out_adjacent_vertices("ORD"):
        print(vertex.element())

    print("DFW degrees: ")
    print(graph.in_degree("DFW"))
    print(graph.degree("DFW"))
    print("---")
    for edge in graph.in_incident_edges("DFW"):
        print(edge.element())
    print("---")
    for edge in graph.out_incident_edges("DFW"):
        print(edge.element())
    print("---")
    for vertex in graph.in_adjacent_vertices("DFW"):
        print(vertex.element())
    print("---")
    for vertex in graph.out_adjacent_vertices("DFW"):
        print(vertex.element())
    print("---")
    print("Edge for UA 877 ")
    for vertex in graph.adjacent_vertices("UA 877"):

        print(vertex.element())

    print("Is adjacent")
    print(graph.are_adjacent("LAX", "SFO"))
    print(graph.are_adjacent("SFO", "LAX"))
    print(graph.are_adjacent("SFO", "JFK"))
    print(graph.are_adjacent("MIA", "JFK"))
    return graph

def visualize_digraph(edge_list_graph):
    G = nx.DiGraph()
    for vertex in edge_list_graph.vertices():
        G.add_node(vertex.element(), name=f"{vertex.element()}")
    for edge in edge_list_graph.edges():
        G.add_edge(edge.vertices[0].element(), edge.vertices[1].element(), name=str(edge.element()))
    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1, \
            node_size=500, node_color='blue', alpha=0.9, \
            connectionstyle='arc3, rad = 0.05',
            labels={node: node for node in G.nodes()})
    edge_labels = dict([((n1, n2), d['name'])
                        for n1, n2, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, font_color='red',
                                 edge_labels=edge_labels)
    plt.axis('off')
    plt.show()


def visualize_ungraph(edge_list_graph, draw_edge=False):
    G = nx.Graph()
    for vertex in edge_list_graph.vertices():
        G.add_node(vertex.element(), name=f"{vertex.element()}")
    for edge in edge_list_graph.edges():
        G.add_edge(edge.vertices[0].element(), edge.vertices[1].element(), name=edge.element())
    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1, \
            node_size=500, node_color='blue', alpha=1, \
            labels={node: node for node in G.nodes()})
    if draw_edge:
        edge_labels = dict([((n1, n2), d['name'])
                            for n1, n2, d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos, font_color='red',
                                     edge_labels=edge_labels)
    plt.axis('off')
    plt.show()


#flight_di_graph = create_weighted_graph()
#visualize_ungraph(flight_di_graph, draw_edge=True)


