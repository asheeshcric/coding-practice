"""
Given a binary tree root, a node X in the tree is named good 
if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_good_nodes(self, node, max_val, count):
        if node is None:
            return

        if node.val >= max_val:
            count[0] += 1
            max_val = node.val

        self.find_good_nodes(node.left, max_val, count)
        self.find_good_nodes(node.right, max_val, count)

    def goodNodes(self, root: TreeNode) -> int:
        # Since, lists are mutable data structures and can be passed by reference
        count = [0]
        self.find_good_nodes(root, max_val=root.val, count=count)
        return count[0]


if __name__ == "__main__":
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=3)
    root.left.left = TreeNode(val=4)
    root.right.right = TreeNode(val=5)

    sol = Solution()
    print(sol.goodNodes(root))
