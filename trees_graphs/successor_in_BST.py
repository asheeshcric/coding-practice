"""
Definition for a binary tree node.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        # write your code here
        current = root
        visited = []
        while current.val != p.val:
            if p.val < current.val:
                current = current.left
                visited.append((current, 'from_right'))
            else:
                current = current.right
                visited.append((current, 'from_left'))

        if current.right is not None:
            # The node has a right branch and the left-most node in the right branch
            # is its successor
            current = current.right
            while current.left is not None:
                current = current.left

            return current

        # If no right branch is found
        parent, direction = visited.pop()
        if direction == 'from_right':
            return parent
        else:
            # Need to move to the top until 'from_right is encountered'
            for parent, direction in visited[::-1]:
                if direction == 'from_right':
                    break

            return parent
