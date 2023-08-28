"""
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. 
You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.
"""

from typing import List
from heapq import heappop, heappush


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        # Sort the pairs list based on the values of nums2 (descending order)
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        # Create a minHeap that contains k elements from nums1
        min_heap = []

        # Track a running sum of the nums from nums1
        n1_sum = 0
        result = 0

        for n1, n2 in pairs:
            heappush(min_heap, n1)
            n1_sum += n1

            # Remove the min if the length of the heap exceeds k
            if len(min_heap) > k:
                n1_pop = heappop(min_heap)
                n1_sum -= n1_pop

            if len(min_heap) == k:
                # If we have enough elements in the heap, update the result
                # Since we're going in descending order based on nums2, n2 is always going to the min
                # num we've reached currently in nums2
                result = max(result, n1_sum * n2)

        return result
