"""
Validate a Binary Search Tree
"""


def is_valid_BST(root):
    return check_validity(root, float("inf"), float("-inf"))


def check_validity(root, max_val, min_val):
    if root is None:
        return True

    if root.val >= max_val or root.val <= min_val:
        return False

    return check_validity(
        root.left, max_val=root.val, min_val=min_val
    ) and check_validity(root.right, max_val=max_val, min_val=root.val)
