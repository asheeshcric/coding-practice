from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total_sum = 0
        for idx, num in enumerate(arr):
            prefix = [num]
            total_sum += self.subarray_sum(arr, idx, prefix)

        return total_sum

    def subarray_sum(self, arr, idx, prefix) -> int:
        current_sum = 0
        # We start with the current prefix at "idx" and find more contiguous subarrays
        for k in range(idx + 1, len(arr)):
            pass
