"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

"""

from collections import deque
from typing import Optional, List


"""
1. Use BFS to retrieve all the nodes in the current level
2. Next, pop from the left of the queue until you reach the rightmost node
3. Store the rightmost node in the resulting list
4. Return when queue is empty
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        queue = deque([root])

        while queue:
            right_node = None
            len_queue = len(queue)
            for _ in range(len_queue):
                # For each level, we want to pop all the nodes
                # and only keep track of the rightmost node
                node = queue.popleft()
                if node:
                    right_node = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_node:
                right_view.append(right_node.val)

        return right_view
