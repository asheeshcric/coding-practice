from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
U:
- Keep track of the coordinates of each node and group them based on the Y-coordinate -- Pre-order traversal
- Again, within each group, store the node's value along with the X-coordinate
- Within a group, if X-coordinates match, order them based on their values

"""


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.positions = defaultdict(list)
        self.preOrder(root)
        print(self.positions)
        result = []
        sorted_coord = list(self.positions.keys())
        sorted_coord.sort()
        for i in sorted_coord:
            self.positions[i].sort(key=lambda x: (x[1], x[0]))
            result.append([k[0] for k in self.positions[i]])

        return result

    def preOrder(self, root, coord=(0, 0)):
        if not root:
            return

        self.positions[coord[1]].append((root.val, coord[0]))
        self.preOrder(root.left, coord=(coord[0]+1, coord[1]-1))
        self.preOrder(root.right, coord=(coord[0]+1, coord[1]+1))
