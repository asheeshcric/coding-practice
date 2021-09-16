from typing import List

"""
1. Start from any node in the graph.
2. Color it with one of the colors
3. Use DFS to traverse to its neighbors and color all the neighbors with the opposite color
4. In the process, if you find any node that is already colored with the same color, this means the graph is not bipartite and return False
5. If all the nodes are colored by the rule, return True at the end


"""


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = dict()

        # Do a DFS from each node in the graph if they are not colored already
        for node in range(len(graph)):
            if node in colors:
                # ALready colored
                continue

            stack = [node]
            colors[node] = True
            while len(stack) > 0:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in colors:
                        colors[neighbor] = not colors[node]
                        stack.append(neighbor)
                    else:
                        if colors[neighbor] == colors[node]:
                            # Same color detected, so not bipartite
                            return False

        return True
