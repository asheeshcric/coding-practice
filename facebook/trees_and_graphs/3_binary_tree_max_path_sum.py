from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        We will need to do a DFS from the root node
        1. For each child of the current node, find the max possible path sum for two cases:
        a. One way is, we can either split the path from the current node and see if it results to max value
        b. Or, we can just follow one of the paths from the current node, i.e. either to the left or to the right
            - This is the sum that we return to the parent node
        c. So, whichever yields the max sum, we store that as our result.
        """
        # Just to store result in a variable that can be accessed from this function, we will use a list
        result = [float("-inf")]

        def dfs(root):
            if root is None:
                return 0

            # We need max sum for the left and right paths from the current node
            leftSum = dfs(root.left)
            rightSum = dfs(root.right)

            # We know that -ve values will only decrease the sum. So, we need to avoid those values
            leftSum, rightSum = max(leftSum, 0), max(rightSum, 0)

            # Now assume that you split the path from the current node
            # This means we take the leftPath and follow the right path going through the current node
            result[0] = max(leftSum + rightSum + root.val, result[0])

            # Also, while returning a path sum to the parent node, we don't split the path from the current node
            # So, we just return the max possible sum from the current node without splitting the path
            return root.val + max(leftSum, rightSum)

        dfs(root)

        return result[0]
