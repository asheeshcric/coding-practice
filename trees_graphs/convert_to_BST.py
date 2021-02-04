# Definition for a binary tree node.
from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Maximum possible height that cannot be exceeded
        # In every recursive call, divide the list into left part and right part of the root node
        # Then construct individual BSTs for both parts

        def convert_to_BST(left, right):
            if left > right:
                return None

            mid = (left+right) // 2
            root = TreeNode(val=nums[mid])
            root.left = convert_to_BST(left, mid-1)
            root.right = convert_to_BST(mid+1, right)
            return root

        return convert_to_BST(0, len(nums)-1)
