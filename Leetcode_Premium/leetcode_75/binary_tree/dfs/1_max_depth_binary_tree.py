"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Solution:
    def maxDepth(self, root: Optional[TreeNode], max_depth=0) -> int:
        if root is None:
            return max_depth

        return max(
            self.maxDepth(root.left, max_depth + 1),
            self.maxDepth(root.right, max_depth + 1),
        )


root = TreeNode()

sol = Solution()
print(sol.maxDepth(root))
