"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(node):
            if node is None:
                return None

            if node.val == p.val or node.val == q.val:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                # This means the current node is the LCA of p and q
                return node

            # Else either p or q is the LCA of the other
            return left if left else right

        return dfs(root)


if __name__ == "__main__":
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=3)
    root.left.left = TreeNode(val=4)
    root.right.right = TreeNode(val=5)

    p = TreeNode(val=2)
    q = TreeNode(val=3)

    sol = Solution()

    print(sol.lowestCommonAncestor(root, p, q))
