# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
U:
- Find the kth smallest number in the tree (smallest when k=1)

M:
- Inorder traversal of BST yields in a sorted list (ascending order)


"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder_list = []
        self.inorder(root)
        return self.inorder_list[k - 1]

    def inorder(self, root):
        if root is None:
            return

        if root.left:
            self.inorder(root.left)

        self.inorder_list.append(root.val)

        if root.right:
            self.inorder(root.right)
