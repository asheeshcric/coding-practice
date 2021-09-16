# Definition for a Node.
from typing import List, no_type_check_decorator


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Key idea: If we can do an in-order traversal of the BST, the order of the nodes will be sorted (from left to right)

Given that: we need to convert the tree into doubly linked-list in-place

1. Initialize variables "first" and "last" that track the head and the most recently processed node
2. In the dfs function, traverse in-order to the tree.
3. When you reach the leftmost element (which is the smallest):
    - Assign that node as the first node in the list
4. Keep backtracking and adding nodes to the list until you reach the final node (rightmost) in the tree
5. Add connections between the first and the last to make it a circular doubly linked list

"""


class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        def dfs(node):
            nonlocal last, first
            if node:
                dfs(node.left)
                if last:
                    # This means we have already processed the first node (lowest element)
                    last.right = node
                    node.left = last
                else:
                    # We encountered the leftmost node in the tree (which is the smallest and the first node in the list)
                    first = node

                last = node
                dfs(node.right)

        if root is None:
            return None

        last, first = None, None
        dfs(root)
        # Finally, connect the first and last node in the list
        first.left = last
        last.right = first
        return first
