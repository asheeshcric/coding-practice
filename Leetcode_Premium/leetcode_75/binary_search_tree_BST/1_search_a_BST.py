"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and 
return the subtree rooted with that node. If such a node does not exist, return null.



"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None:
            if val < root.val:
                # Go to the left tree
                root = root.left
            elif val > root.val:
                # Go to the right branch
                root = root.right
            else:
                return root

        return None
