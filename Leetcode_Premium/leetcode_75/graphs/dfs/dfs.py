# Keep going down until you reach a leaf node in the graph and traverse back


def dfs(graph, node, visited):
    if node not in visited:
        # First time visiting the node
        visited.add(node)
        print(f"Visited Node: {node}")
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    visited = set()

    dfs(graph, node="A", visited=visited)
