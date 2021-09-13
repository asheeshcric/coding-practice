# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
The idea is to use a BFS and go through each level and find the rightmost node`

Keep on adding children to the queue, but for each level keep track of how many nodes were there in the beginning
This way, you know which one is the rightmost element for that level
Once you reach the rightmost element, you add it to the result and repeat the same process again

"""


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = [root]
        result = []
        while len(queue) > 0:
            # For each level, track how many nodes are in the queue
            # With this, we know that the last node (rightmost) is the one that needs to be added to the result
            queue_len = len(queue)
            for i in range(queue_len):
                current = queue.pop(0)
                if i == queue_len - 1:
                    # We know that this is the rightmost node for that particular level
                    result.append(current.val)

                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

        return result
