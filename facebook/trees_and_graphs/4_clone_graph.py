# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


"""
# First we create a hashMap that keeps track of a new clone for each node in the graph
# Then we do a dfs, creating new copies of each node and adding the neighbors to the node
So, basically, the idea is to keep track of the cloned copies that you've already created. This makes sure that you don't create additional copies of the same node
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        # Base case
        if node is None:
            return None

        oldToNew = dict()

        def dfs(node):
            # If the node is already cloned, just return the cloned node
            if node in oldToNew:
                return oldToNew[node]

            # Else create a clone
            new_copy = Node(val=node.val)
            oldToNew[node] = new_copy
            # Add all the neighbors of that node to its cloned version
            for neighbor in node.neighbors:
                new_copy.neighbors.append(dfs(neighbor))

            return new_copy

        return dfs(node)
