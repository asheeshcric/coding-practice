from typing import List

"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.



We use a hashmap to keep track of all the prefix sums that we've encountered so far
1. This means for current sum of the subarray, if we have a prefix sum that we've already calculated and that happens to be current_sum - k, then
we can chop off that portion of the array to still get to the required sum
2. Hence, we keep on looking how many prefix_sums we can add up to in order to satisfy the given target

It's using the property:
    - sum(i, j) = sum(0, j) - sum(0, i)
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        total = 0
        res = 0
        for num in nums:
            total += num
            res += prefix_sum.get(total - k, 0)
            prefix_sum[total] = prefix_sum.get(total, 0) + 1

        return res
