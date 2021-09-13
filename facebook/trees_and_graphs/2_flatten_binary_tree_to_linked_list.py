"""
Convert binary tree to linked list using pre-order traversal.

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pre_order(self, root, nodes=[]):
        if root is not None:
            nodes.append(root.val)
        if root.left is not None:
            self.pre_order(root.left, nodes)
        if root.right is not None:
            self.pre_order(root.right, nodes)

        return nodes

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Need to find a recursive way of handling the Tree nodes in pre-traversal order
        nodes = self.pre_order(root)
        for node in nodes[1:]:
            if root is None:
                break
            root.left = None
            root.right = TreeNode(node)
            root = root.right
