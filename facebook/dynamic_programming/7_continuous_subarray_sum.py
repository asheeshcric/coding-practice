"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

"""

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int):
        # By default, we have already seen a sum of "0" before looping through the array i.e, at index -1
        seen_indices = {0: -1}
        remainder = 0
        """
        The idea is accumulate the sum as we loop through array.
        Find the remainder of the current sum when you divide by k
        If the remainder is previously seen and has an index "j" such that i-j > 1, return True
        Else keep on going until the end of the array
        Return False

        NOTE: Instead of having the remainder as key in the map, we can use the actual sum, but that takes a lot of space if the number are huge
        So, the remainder will take less memory compared the actual sum
        """
        for i, num in enumerate(nums):
            remainder += num
            remainder = remainder % k
            if remainder in seen_indices:
                if i - seen_indices[remainder] > 1:
                    return True
            else:
                seen_indices[remainder] = i

        return False
