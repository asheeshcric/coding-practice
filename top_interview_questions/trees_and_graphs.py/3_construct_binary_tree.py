"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.


U:
- Preorder and inorder traversals of the same tree are given
- The problem is you are not given "Null" nodes in the traversals
- Return the root node of the formed binary tree

M:
- Preorder (root, left, right)
- Inorder (left, root, right)

e.g: 
        3
    |       |
    9       20
        |       |
        15      7

For the above tree
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

- We know that the first node in the preorder is always the root and the second node is the root of the left subtree
- If we know what our root node is, then we can find the nodes that would go to the left and right subtree using the inorder list

Here, "3" is the root node. So, find the index of "3" in the inorder list (which is 1)
    - Every node to the left of "3" will be in the left subtree
    - Every node to the right of "3" will be in the right subtree

root = TreeNode(preorder[0])        # root = 3
root_idx = inorder.index(preorder[0]) # which is 1 in the first call
# The left subtree will contain root_idx nodes
root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])

"""
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])

        # We know which elements are to the left of the root and which are to the right of the root
        # by looking at the inorder list
        root.left = self.buildTree(preorder[1 : root_idx + 1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx + 1 :], inorder[root_idx + 1 :])

        return root
