from collections import deque

def bfs(graph, queue, visited):
    if queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            queue.append(neighbor)
        if node not in visited:
            print(node)
        visited.add(node)
        bfs(graph, queue, visited)


if __name__ == '__main__':
    # Define a graph with adjacency lists for each node
    # The graph below is a directed graph
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': [] 
    }
    queue = deque()
    queue.append('A')
    visited = set()
    bfs(graph, queue, visited)