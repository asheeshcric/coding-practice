class Node:

    def __init__(self, value=None, neighbors=None):
        self.value = value
        self.neighbors = neighbors
        self.visited = False


def build_graph(nodes_from, nodes_to):
    """
    Takes two lists containing edges from one node to other nodes
    Returns a dictionary with adjacency lists for each node in the graph
    """
    graph = dict()
    for idx, node_from in enumerate(nodes_from):
        node_to = nodes_to[idx]
        if node_from not in graph:
            graph[node_from] = [node_to]
        else:
            graph[node_from].append(node_to)

        # If the graph is bidirectional
        if node_to not in graph:
            graph[node_to] = [node_from]
        else:
            graph[node_to].append(node_from)

    return graph


visited = set()


def dfs(graph, root, visited):
    if root not in graph:
        return

    for neighbor in graph[root]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(graph, neighbor, visited)


def bfs(graph, root):
    if root not in graph:
        return
    visited = set()
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)
