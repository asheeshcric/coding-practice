"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value
and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.
"""
from typing import List
import statistics


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Use a sliding window to keep track of the sum
        For each iteration, substract the removed item from the window and add the new
        item added to the window
        In the end, take the average and return it
        """
        start = 0
        max_sum = -float("inf")
        while start + k <= len(nums):
            if start == 0:
                window_sum = sum(nums[start : start + k])
            else:
                window_sum = window_sum - nums[start - 1] + nums[start + k - 1]

            if window_sum > max_sum:
                max_sum = window_sum

            start += 1

        return max_sum / k
