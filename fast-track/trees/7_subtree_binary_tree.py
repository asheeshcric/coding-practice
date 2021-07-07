"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


Solution:
1. Serial both trees into an encoded string.
2. Check if sub_tree's string is present in the main tree's string.
"""


def path_string(node, string_path):
    if node is None:
        return string_path + "*"

    string_path += "_" + str(node.val)
    string_path = path_string(node.left, string_path)
    string_path = path_string(node.right, string_path)
    return string_path


def isSubtree(s, t) -> bool:
    path_s = path_string(s, "")
    path_t = path_string(t, "")
    print(path_s, path_t)
    return path_t in path_s
