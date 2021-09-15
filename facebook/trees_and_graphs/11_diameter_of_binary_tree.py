from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
- Using a bottom-up approach, find the height and diameter of each node -- starting from the leaf nodes
- For each node, take the max height comparing its left and right subtree
- Calculate the diameter in the similar way

- Null node's height is considered as -1
- Leaf node's height is considered as 0
- When calculating the height of the current node, we add 1 to the height of the subtree (left or right, whichever is greater)
- For diameter, it is the number of children nodes that the root node has. So, this equals to diameter = 2+left_height+right_height

"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]

        def find_height(root):
            # For a null node, the height is considered to be -1
            if root is None:
                return -1

            left_height = find_height(root.left)
            right_height = find_height(root.right)

            max_diameter[0] = max(max_diameter[0], 2 + left_height + right_height)

            return 1 + max(left_height, right_height)

        find_height(root)
        return max_diameter[0]
