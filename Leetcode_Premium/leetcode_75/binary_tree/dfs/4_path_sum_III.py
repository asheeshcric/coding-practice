"""
Given the root of a binary tree and an integer targetSum, return the number of paths 
where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, 
but it must go downwards (i.e., traveling only from parent nodes to child nodes).

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        The idea is to backtrack from the leaf nodes
        DFS to go down a path, then while coming up, keep adding node values
        to check if it's equal to the target sum
        Remove the node from the current_path once you're done with it
        """
        count = [0]
        current_path = []

        def dfs(node, current_path):
            if node is None:
                return

            current_path.append(node.val)
            path_sum = 0
            for node_val in current_path[::-1]:
                path_sum += node_val
                if path_sum == targetSum:
                    count[0] += 1

            dfs(node.left, current_path)
            dfs(node.right, current_path)

            del current_path[-1]

        dfs(root, current_path)
        return count[0]


if __name__ == "__main__":
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=3)
    root.left.left = TreeNode(val=4)
    root.right.right = TreeNode(val=5)

    sol = Solution()
    print(sol.pathSum(root, targetSum=5))
