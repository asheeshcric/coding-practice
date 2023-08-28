"""
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort the intervals (ascending) based on the right value
        intervals = sorted(intervals, key=lambda i: i[1], reverse=False)

        # Assume that we start from -inf, and keep increasing our right limit as
        # we go through the intervals
        # If any range overlaps with the right limit, we remove it
        right_limit = -float("inf")
        result = 0

        for left, right in intervals:
            if left >= right_limit:
                # This means this interval does not overlap with the current right_limit,
                # Hence, doesn't need to be removed
                right_limit = right

            else:
                # Overlaps and needs to be removed
                result += 1

        return result
