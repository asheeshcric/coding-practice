from typing import List


"""
U:
- Find the rooted nodes that will result in minimum height of the tree (there can be multiple such nodes)
- Input: n (number of nodes) and (n-1) edges as a list of lists
- 1 <= n <= 2*10^4

M:
- First, build an adjacency list for the graph
- For each node, traverse through the node to find the max height of the tree
    - While doing so, keep track of the min height of the tree

- Return the nodes that have the min height(s)


"""
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Base case:
        if n <= 2:
            return [i for i in range(n)]

        graph = self.getAdjacencyList(n, edges)

        # Initialize the first layer of leaf nodes in the graph (i.e. ones that have only one layer)
        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)

        # The idea is to keep trimming the leaves until we reach the centroid nodes (which is our result)
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []

            while leaves:
                leaf = leaves.pop()
                # Since it is a leaf, it has only one neighbor which we pop out
                neighbor = graph[leaf].pop()
                # Now, remove the leaf node from the neighbor's list
                graph[neighbor].remove(leaf)
                # Check if the neighbor only has one neighbor now
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        # The remaining leaves are the centroids of the tree
        return leaves

    def getAdjacencyList(self, n, edges):
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        return graph
