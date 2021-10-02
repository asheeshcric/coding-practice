# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Inorder Traversal: left, root, right
Pre-order Traversal: root, left, right
Postorder Traversal: left, right, root
Level Order Traversal: BFS
"""


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if root is None:
            return

        if root.left:
            self.inorder(root.left)

        self.result.append(root.val)

        if root.right:
            self.inorder(root.right)
