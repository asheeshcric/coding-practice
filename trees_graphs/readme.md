### Trees

1. Binary Tree
    - A tree in which each node has up to two children (other than that, all trees are ternary trees)
    - Types: Complete, Full, and Perfect

        a. A complete binary tree is a binary tree in which every level of the tree is fully filled, except for perhaps the last level. To the extent that the last level is filled, it is filled left to right.
        b. A full binary tree is a binary tree in which every node has either zero or two children. That is, no nodes have only one child.
        c. A perfect binary tree is one that is both full and complete. All leaf nodes will be at the same level, and this level has the maximum number of nodes

2. Binary Search Tree
    - A binary tree in which every node fits a specific ordering property:
        - `All left descendants <= n < all right descendants`
        - This must be true for each node 'n'

3. Binary Tree Traversal

    a. In-order traversal:

        - Visit the left branch, then the current node, and finally, the right branch

    b. Pre-order traversal:

        - Visit the current node before its child nodes

    c. Post-order traversal:

        - Visit the current node after its child nodes

4. Binary Heaps (Min-Heaps and Max-Heaps)
    - A min-heap is a complete binary tree where each node is smaller than its children
    - The root node is the minimum element in the tree
    - `insert` and `extract_min (heapify)` are two main operations in a min-heap (need to maintain the min-heap property after each operation)
    - `O(1)`: find_max
    - `O(lg n)`: insert
    - `O(lg n)`: delete


5. Tries (Prefix Trees)
    - Stores words as characters in the form of a tree
    - Used to validate if a word is in a dictionary or not


