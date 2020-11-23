class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.n_vertices = len(graph.keys())

    def topological_sort_util(self, visited, stack, node):
        visited[node] = True

        # Traverse through all the neighbors of the node
        for neighbor_node in self.graph[node]:
            if visited[neighbor_node] is False:
                self.topological_sort_util(visited, stack, neighbor_node)

        # Push the last visited node the stack in recursive order
        stack.insert(0, node)
        return stack, visited

    def topological_sort(self):
        visited = {node: False for node in self.graph.keys()}
        stack = []
        for node in self.graph.keys():
            if visited[node] is False:
                stack, visited = self.topological_sort_util(visited, stack, node)
        return stack


if __name__ == '__main__':
    """
    Graphs where certain events have to occur first
    e.g. Class prerequisites, Event scheduling, Program dependencies
    """
    graph_dict = {
        'C': ['F'],
        'D': [],
        'A': ['B', 'C'],
        'E': ['F'],
        'F': [],
        'B': ['D', 'E'],
    }
    graph = Graph(graph=graph_dict)
    stack = graph.topological_sort()
    print(f'Topological sorted stack: {stack}')
