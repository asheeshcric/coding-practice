from typing import Optional

"""
1. Track the max and min values that can be allowed wherever you traverse through the tree
2. If you reach the leaf node, it means the tree is valid on that branch

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def validate(self, root, max=float("inf"), min=float("-inf")):
        if root is None:
            return True

        if root.val >= max or root.val <= min:
            return False

        return self.validate(root.left, max=root.val, min=min) and self.validate(
            root.right, max=max, min=root.val
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)
