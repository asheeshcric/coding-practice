"""
Given the root of a binary tree, the level of its root is 1,
the level of its children is 2, and so on.

Return the smallest level x such that 
the sum of all the values of nodes at level x is maximal.

"""


from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Since the tree will have atleast one level
        level = 0
        queue = deque([root])
        max_sum = root.val
        max_level = 1

        while queue:
            level_sum = 0
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                # Avoid adding Null nodes to the queue
                # (since we don't want final level to have all NULL nodes)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_level = level
                max_sum = level_sum

        return max_level
