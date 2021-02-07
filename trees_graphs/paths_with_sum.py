# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def path_with_root(self, root, target):
        if root is None:
            return 0

        num_paths = 0
        if root.val == target:
            num_paths += 1

        num_paths += self.path_with_root(root.left, target-root.val)
        num_paths += self.path_with_root(root.right, target-root.val)

        return num_paths

    def pathSum(self, root: TreeNode, k: int) -> int:
        if root is None:
            return 0

        return self.pathSum(root.left, k) + self.pathSum(root.right, k) + self.path_with_root(root, k)
