"""
Determine if two trees are identical or not
"""


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


def identical_trees(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is not None:
        if root1.data != root2.data:
            return False
        left_part = identical_trees(root1.left, root2.left)
        right_part = identical_trees(root1.right, root2.right)
        return left_part and right_part
    else:
        return False


def main():
    root1 = create_tree()
    root2 = create_tree()
    print(identical_trees(root1, root2))
    print(identical_trees(root1, root1))


if __name__ == "__main__":
    main()


# --------------End of Boiler Code----------------
