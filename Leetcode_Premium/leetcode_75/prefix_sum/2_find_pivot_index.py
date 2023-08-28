"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers 
strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 
because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 1. Get the total sum of nums
        # 2. Start from the left and keep adding the numbers
        # 3. At each iteration with number x, compare (left_sum == total - leftsum - x)
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num

        return -1
