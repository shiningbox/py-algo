from collections import deque

# Toplogical sort a graph
# Use
def toplogical_sorting(edge_list) -> list:
    nodes = set()
    res = []
    g = {}
    for edge in edge_list:
        nodes.add(edge[0])
        nodes.add(edge[1])
        if edge[0] not in g:
            g[edge[0]] = []
        if edge[1] not in g:
            g[edge[1]] = []
        g[edge[0]].append(edge[1])

    size = len(nodes)
    ins = [0] * size
    queue = deque()
    # Find incoming values for ins
    for edge in edge_list:
        ins[edge[1]] += 1

    for i in ins:
        if ins[i] == 0:
            queue.append(i)
    print(g)
    while queue:
        # pop the head with incoming == 0
        head = queue.popleft()
        res.append(head)
        # Now disconnect head with its ongoing nodes
        for neighbor in g[head]:
            ins[neighbor] -= 1
            # Push the neighbor with incoming == 0 to the queue
            if ins[neighbor] == 0:
                queue.append(neighbor)
    return res


edge_list = [(0, 1), (1, 2), (2, 5), (1, 3), (3, 4), (1, 6), (4, 6), (4, 5), (5, 7)]
print(toplogical_sorting(edge_list))
