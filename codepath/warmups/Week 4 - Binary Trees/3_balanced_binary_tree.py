"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
    - a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

U: 
- Given root of a binary tree, check if left and right subtrees of each node in the tree differ no more than 1

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return (
            abs(self.height(root.left) - self.height(root.right)) <= 1
            # Now do this for both the left and right subtrees
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def height(self, root) -> int:
        if root is None:
            return -1

        return 1 + max(self.height(root.left), self.height(root.right))
