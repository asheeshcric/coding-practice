"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def create_graph(adj_list) -> Node:
    # Implement this to create a graph from the adjacency list
    return Node()


def dfs(node, node_neighbors):
    if node.val in node_neighbors:
        # return the new node that we already created for that value
        return node_neighbors[node.val]

    new_copy = Node(val=node.val)
    node_neighbors[node.val] = new_copy
    for neighbor in node.neighbors:
        new_copy.neighbors.append(dfs(neighbor, node_neighbors))

    return new_copy


def clone_graph(node) -> Node:
    if node is None:
        return None

    node_neighbors = dict()

    dfs(node, node_neighbors)


if __name__ == "__main__":
    adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
    node = create_graph(adj_list)
    new_root = clone_graph(node)
    print(new_root)
