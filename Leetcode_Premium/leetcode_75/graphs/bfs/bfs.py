# Explore the current node's all branches before moving to the next one
# As you visit a node, keep all its neighboring nodes in the queue
# and keep popping from the left


from collections import deque


def bfs(graph, queue, visited):
    if queue:
        node = queue.popleft()
        if node not in visited:
            print(f"Visiting node: {node}")
        visited.add(node)
        for neighbor in graph[node]:
            queue.append(neighbor)

        bfs(graph, queue, visited)


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
    visited = set()
    queue = deque()

    queue.append("A")
    bfs(graph, queue, visited=visited)
