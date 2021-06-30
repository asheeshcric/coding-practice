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


def print_tree(node, level=0):
    # The structure is not printed well though
    if node != None:
        print_tree(node.left, level + 1)
        print(" " * 4 * level + "->", node.data)
        print_tree(node.right, level + 1)


def in_order_traversal(root, result):
    if root is not None:
        if root.left is not None:
            in_order_traversal(root.left, result)
        result.append(root.data)
        if root.right is not None:
            in_order_traversal(root.right, result)

    return result


def pre_order_traversal(root, result):
    if root is not None:
        result.append(root.data)
        if root.left is not None:
            pre_order_traversal(root.left, result)
        if root.right is not None:
            pre_order_traversal(root.right, result)

    return result


def post_order_traversal(root, result):
    if root is not None:
        if root.left is not None:
            post_order_traversal(root.left, result)
        if root.right is not None:
            post_order_traversal(root.right, result)
        result.append(root.data)

    return result


def add_to_queue(queue, node):
    if node.left is not None:
        queue.append(node.left)
    if node.right is not None:
        queue.append(node.right)
    return queue


def level_order_traversal(root, result, queue):
    result.append(root.data)
    queue = add_to_queue(queue, root)
    while len(queue) > 0:
        node = queue.pop(0)
        result.append(node.data)
        queue = add_to_queue(queue, node)

    return result


def main():
    root = create_tree()
    print_tree(root)

    result = []
    print(in_order_traversal(root, result))
    result = []
    print(pre_order_traversal(root, result))
    result = []
    print(post_order_traversal(root, result))
    result = []
    queue = []
    print(level_order_traversal(root, result, queue))


if __name__ == "__main__":
    main()
