# -----------------Boiler Code----------------

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


def invert_tree(root):
    if root is None:
        return root

    original_root = root
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return original_root


def main():
    root = create_tree()
    inverted_tree = invert_tree(root)


if __name__ == "__main__":
    main()


# --------------End of Boiler Code----------------
