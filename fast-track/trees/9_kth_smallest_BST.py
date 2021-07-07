"""
BST is arranged in in-order fashion for ascending order numbers
So, in-order traversal would arrange it in ascending order, and we can then take the (k-1)th index to get the kth smallest element
"""


def in_order_traversal(root, result):
    if root is not None:
        in_order_traversal(root.left, result)
        result.append(root.val)
        in_order_traversal(root.right, result)

    return result


def kth_smallest(root, k):
    sorted_array = in_order_traversal(root)
    return sorted_array[k - 1]
