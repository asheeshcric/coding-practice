# class TreeNode:
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, maxi=float("inf"), mini=float("-inf"))

    def isValid(self, root, maxi, mini):
        if root is None:
            return True

        if not (root.val < maxi and root.val > mini):
            return False

        return self.isValid(root.left, maxi=root.val, mini=mini) and self.isValid(
            root.right, maxi=maxi, mini=root.val
        )
