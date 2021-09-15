# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        # Base case: if the root value matches one of p or q, we don't go below that node
        if root.val == p.val or root.val == q.val:
            return root

        left, right = None, None

        # Check on the left side of the current root
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)

        # Also, check on the right side of the current root to see if there's a match
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # Two cases: if it returns both left and right, we know that we found the LCA
        # Else: we just found one of p or q. So, we return that node instead of None to go up higher again to find the LCA
        if left and right:
            return root

        else:
            # We return the node that matched with either p or q
            return left or right
