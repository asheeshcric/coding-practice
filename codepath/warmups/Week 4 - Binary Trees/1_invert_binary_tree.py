from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                # Add children of the node to the queue
                queue.append(node.left)
                queue.append(node.right)

                # Swap left with right if the current is not None
                node.left, node.right = node.right, node.left

        return root
