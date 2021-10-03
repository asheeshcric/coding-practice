"""
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
If the given node has no in-order successor in the tree, return null.
The successor of a node p is the node with the smallest key greater than p.val.

U:
- Given a BST, and a node p (with val=p.val), find another node that is just greater than p (i.e. next greater value than p.val)
- If no such node exists, return None

M:
- Traverse BST, using the value of p
if p.val >= root.val:
    # There's no point in going to the left
    # because left will contain all values less than p.val
    # Go to the right
else:
    # Either root is the node or somewhere from the left subtree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: "TreeNode", p: "TreeNode") -> "TreeNode":
        if root is None:
            return None

        result = TreeNode(float("inf"))
        while True:
            if p.val >= root.val:
                # This means the node can only be on the right subtree
                if root.right:
                    root = root.right
                else:
                    # No node greater than p.val exists
                    return result if result.val != float("inf") else None
            else:
                if result.val > root.val:
                    result = root
                if not root.left:
                    # Current root will be the successor
                    return result if result.val != float("inf") else None
                else:
                    root = root.left
