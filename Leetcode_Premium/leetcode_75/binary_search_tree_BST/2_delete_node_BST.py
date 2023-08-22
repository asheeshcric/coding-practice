"""
Given a root node reference of a BST and a key, 
delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Three cases:

1. If the node we want to delete doesn't have a left child
    - We return the right child node directly and replace the deleted node with it

2. If the node to be deleted doesn't have a right child
    - We replace the deleted node with the left child node

3. If it has both children
    - Then, we only go to the right subtree and find the minimum node for it to be replace the deleted node
    - Then we recursively delete the right child of the deleted node and keep doing so until all the values
    are updated in the right subtree. This will ensure that the right subtree is still a valid BST
"""


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if key < root.val:
            # It means the node to be deleted is on the left subtree
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            # It is on the right subtree
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None:
                # Simply, return the right child and replace the deleted node with it
                return root.right
            elif root.right is None:
                # Return the left child
                return root.left

            # This is the case where we find the node to be deleted
            # We always go to the right child of the deleted node to find its minimum and replace the deleted node with it
            current = root.right
            while current.left:
                # If you keep going left of the tree, you find the minimum node
                current = current.left

            # Since we want to replace the current deleted root with the found min value
            root.val = current.val

            # Now delete the root of the right subtree as it needs to be updated too
            root.right = self.deleteNode(root.right, root.val)

        return root
