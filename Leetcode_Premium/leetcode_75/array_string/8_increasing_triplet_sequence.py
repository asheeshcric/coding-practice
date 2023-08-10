"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        smallest, second_smallest = float("inf"), float("inf")
        for num in nums:
            if num < smallest:
                smallest = num
            elif num < second_smallest and num > smallest:
                second_smallest = num
            elif num > smallest and num > second_smallest:
                return True

        return False


sol = Solution()
print(sol.increasingTriplet([5, 4, 3, 2, 1]))
