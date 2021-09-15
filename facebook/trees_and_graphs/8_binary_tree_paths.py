"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(root, current_path):
            if root is None:
                return

            # Add this node to the path
            current_path += str(root.val) + "->"

            # Check if it is a leaf node
            if root.left is None and root.right is None:
                result.append(current_path[:-2])
                return

            # Traverse if there's a child below
            if root.left:
                dfs(root.left, current_path)
            if root.right:
                dfs(root.right, current_path)

        dfs(root, "")

        return result
