from typing import List

"""
U:
- You're given a graph with n nodes (labelled 0 to n-1)
- Graph is given as a 2D array where graph[u] is a list of nodes that u is adjacent to
    - No self-edges (graph[u] does not contain u), no parallel edges (no duplicate nodes in graph[u])
    - Graph is undirected, i.e. if v is in graph[u], then u is in graph[v]
    - Graph may not be fully connected

- Check if the graph is bipartite or not. See if the nodes in the graph can be split into two groups such that no two nodes in the same group connect to eachother
    - Every edge in the graph connects a node in set A to a node in set B
- Return True if bipartite else False

- Base cases: Return True if n == 1

M:
- For all neighbors of a node, color them the opposite.
- If you find a node that has already been colored (that too with the same color of the parent node, return False)



"""


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        if n == 1:
            return True

        # True for one color and False for the other color
        colors = dict()

        for node in range(n):
            if node in colors:
                # Already colored
                continue

            stack = [node]
            colors[node] = True
            while stack:
                node = stack.pop()
                for neigh in graph[node]:
                    if neigh not in colors:
                        colors[neigh] = not colors[node]
                        stack.append(neigh)
                    else:
                        if colors[neigh] == colors[node]:
                            return False

        return True
