"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k 
and remove them from the array.

Return the maximum number of operations you can perform on the array.

"""

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        start, end = 0, len(nums) - 1
        num_ops = 0

        while start < end:
            if nums[start] + nums[end] == k:
                # Both numbers can be removed
                num_ops += 1
                start += 1
                end -= 1

            elif nums[start] + nums[end] > k:
                # Need to move the right pointer to decrease the sum
                end -= 1

            else:
                start += 1

        return num_ops
