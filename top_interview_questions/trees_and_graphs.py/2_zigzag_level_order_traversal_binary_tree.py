"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

U:
- Level order is BFS
- Need to return the levels in alternative orders: (left-to-right), then (right-to-left)

M:
- Use a queue for BFS

P:
- A flag that keeps track of whether to create level from left to right or right to left at each level
- queue[root]
- First group nodes based on their levels
- Then reverse the level alternatively (for odd index in the list)


"""
# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
U:
- Return a list of lists containing each level in the tree.
- Levels should be arranged in alternative order (left-right and then right-left)

M:
- Using two stacks, first stores the nodes in one level, second stores the children in another level

P:
- s1 = [root]
- s2 = []
- level = []
- result = []

First go through all nodes in s1:
    - Add that node to the level
    - Append nodes to s2 from left to right children of the nodes in s1
- Add the obtained level to the result and empty level

Now, go through all nodes in s2:
    - Append nodes to s1 from right to left children of the nodes in s2
- Add the obtained level to the result and empty level

"""


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        s1 = [root]
        s2 = []
        level = []
        result = []

        while s1 or s2:
            while s1:
                root = s1.pop()
                # Add the root to that level
                level.append(root.val)
                if root.left:
                    s2.append(root.left)
                if root.right:
                    s2.append(root.right)

            result.append(level)
            level = []
            while s2:
                root = s2.pop()
                level.append(root.val)
                if root.right:
                    s1.append(root.right)
                if root.left:
                    s1.append(root.left)

            if level:
                result.append(level)
                level = []

        return result
