"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

U:
- Move the items of the array k-positions to the right

M:
- Indexing of the list moving them using extra space or in-place

P:
To make sure that k does not exceed the length of the array, we do: k = k % n
Because once you rotate n times, it comes back to the original

1. First method: 
    - Use an extra O(n) space to store one part of the list
    - Reposition the other part in the list
    - Copy the first part to the list

2. Second method:
    - Reverse the list in place
    - Reverse the first part up to [:k]
    - Reverse the second part [k:]


"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead."""
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k :] + nums[: n - k]

    def second_method(self, nums, k) -> None:
        n = len(nums)
        k = k % n

        # First reverse the list
        nums.reverse()
        # Reverse the first part
        nums[:k] = nums[:k][::-1]
        # Reverse the second part
        nums[k:] = nums[k:][::-1]
