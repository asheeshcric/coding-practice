"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.


"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_leaves(self, root, leaves=[]):
        if root is None:
            return

        # First find leaves to the left of the root
        self.find_leaves(root.left, leaves)
        if root.left is None and root.right is None:
            leaves.append(root.val)

        # Then proceed to the right branches
        self.find_leaves(root.right, leaves)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [], []
        self.find_leaves(root1, leaves1)
        self.find_leaves(root2, leaves2)

        return True if leaves1 == leaves2 else False
