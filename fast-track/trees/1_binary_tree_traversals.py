"""
Four ways to traverse a Binary Tree
    - In-order (Left, Root, Right) -- Depth First
    - Pre-order (Root, Left, Right)
    - Post-order (Left, Right, Root)
    - Level order (Breadth First)
"""

import random


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def create_tree() -> Node:
    root = Node(random.randint(0, 10))
    node = root
    for i in range(random.randint(10, 15)):
        if node.left is None:
            node.left = Node(random.randint(0, 100))
        elif node.right is None:
            node.right = Node(random.randint(0, 100))
        else:
            node = node.left if random.randint(0, 10) % 2 == 0 else node.right

    return root


def in_order_traversal(root):
    pass


def pre_order_traversal(root):
    pass


def post_order_traversal(root):
    pass


def level_order_traversal(root):
    pass


def main():
    root = create_tree()

    in_order_traversal(root)
    pre_order_traversal(root)
    post_order_traversal(root)
    level_order_traversal(root)


if __name__ == "__main__":
    main()
