"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, node1, node2):
        if node1 is None and node2 is None:
            # Reached the end on both the sides
            return True

        if node1 is None or node2 is None:
            # One of the subtrees has lesser nodes (so not symmetrical)
            return False

        # Check for alternate left and right subtrees for both the nodes
        return (
            node1.val == node2.val
            and self.isMirror(node1.left, node2.right)
            and self.isMirror(node1.right, node2.left)
        )
