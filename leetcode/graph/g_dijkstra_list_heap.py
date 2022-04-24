from collections import deque
edge_list1 = [(0, 1, 1), (1, 2, 2), (2, 5, 10), (1, 3, 3), (3, 4, 3), (1, 6, 7), (4, 6, 3), (4, 5, 3), (5, 7, 1)]
#edge_list2 = [(0, 1, 1), (1, 2, 2), (2, 5, 10), (1, 3, 3), (3, 4, 3), (1, 6, 7), (4, 6, 3), (4, 5, 3), (5, 7, 1)]


# Gradually building a min distance cloud
# - Starting with the start node s, update the size of the cloud to the distance of its nearest neighbor
# - Move to its nearest neighbor i, continue expanding the cloud with its nearest neighbor j
# - Continue the process
def dijkstra(start, graph: list) -> list:
    node_size = len(graph)




