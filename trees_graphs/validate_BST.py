# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_validity(root, float('inf'), float('-inf'))

    def check_validity(self, root, _max, _min):
        if root is None:
            return True

        if root.val >= _max or root.val <= _min:
            return False

        return self.check_validity(root.left, root.val, _min) and self.check_validity(root.right, _max, root.val)
