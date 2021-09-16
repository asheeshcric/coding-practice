"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right

"""

"""
1. Can use DFS to traverse through the nodes of the tree. When traversing, pass in the row and column value for each level
2. If you go to the left: column - 1, row + 1
   If you go to the right: column + 1, row + 1
3. Keep track of the nodes based on their column and row numbers in a dictionary of dictionary
4. Merge all rows for each column and return the output

"""
from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def add_to_dict(self, column_nodes, column, row, value):
        if column not in column_nodes:
            column_nodes[column] = dict()

        if row in column_nodes[column]:
            column_nodes[column][row].append(value)
        else:
            column_nodes[column][row] = [value]

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        column_nodes = defaultdict(defaultdict)

        def dfs(node, column=0, row=0):
            if node is None:
                return

            self.add_to_dict(column_nodes, column, row, node.val)

            # Go to the left of the node
            dfs(node.left, column - 1, row + 1)

            # Go to the right of the node
            dfs(node.right, column + 1, row + 1)

        dfs(root)
        result = []
        # Now, for each column, the node values must be arranged based on their row values
        for column in sorted(column_nodes.keys()):
            node_vals = []
            for row in sorted(column_nodes[column].keys()):
                node_vals += column_nodes[column][row]

            result.append(node_vals)

        return result
