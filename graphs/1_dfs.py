def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, node=neighbor)

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
    # Create a set to keep track of the visited nodes
    visited = set()
    # Considering 'A' as the starting node in the graph for now
    dfs(visited, graph, node='A')