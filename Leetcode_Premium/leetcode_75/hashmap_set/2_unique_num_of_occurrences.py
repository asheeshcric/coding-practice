"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = dict()
        for num in arr:
            occurrences[num] = occurrences.get(num, 0) + 1

        return len(occurrences.values()) == len(set(occurrences.values()))

    def usingCounter(self, arr: List[int]) -> bool:
        # Simplified approach by directly using Counter
        counts = Counter(arr).values()
        return len(counts) == len(set(counts))
