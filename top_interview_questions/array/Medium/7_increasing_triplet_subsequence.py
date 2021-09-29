"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Understand:
    Inp: A list of numbers
    Out: True if there exists a triplet of indices such that i < j < k and nums[i] < nums[j] < nums[k]

    Edge cases:
        - Check if length of list is greater than 2
        - Also, if there exists no such triplet, return False

Match:

"""

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first_smallest, second_smallest = float("inf"), float("inf")
        for n in nums:
            if n < first_smallest:
                first_smallest = n
            elif n < second_smallest and n > first_smallest:
                second_smallest = n
            elif n > first_smallest and n > second_smallest:
                return True

        return False
