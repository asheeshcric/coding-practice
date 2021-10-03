# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


"""
U:
- We are given a perfect binary tree (with all nodes having two children)
- There's an additional next pointer for each node
- Need to point the next pointer to the adjacent right node in the tree


M:
- It is similar to zigzag level order traversal except for this case, we use two queues and append the right child first

"""
from collections import deque


class Solution:
    def connect(self, root: "Node") -> "Node":
        if root is None:
            return None

        q1 = deque([root])
        q2 = deque()

        while q1 or q2:
            prev = None
            while q1:
                node = q1.popleft()
                node.next = prev
                prev = node

                # Add right child first followed by left child to the other queue
                if node.right:
                    q2.append(node.right)
                if node.left:
                    q2.append(node.left)

            prev = None
            while q2:
                node = q2.popleft()
                node.next = prev
                prev = node

                if node.right:
                    q1.append(node.right)
                if node.left:
                    q1.append(node.left)

        return root
