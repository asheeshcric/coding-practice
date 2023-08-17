"""
Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0

        while right < len(nums):
            if nums[right] == 0:
                # If we encounter a zero while expanding the window, we decrease
                # the remaining available zero flips
                k -= 1

            if k < 0:
                # This means our window start needs to be moved to the right
                if nums[left] == 0:
                    # If 0 was removed from the window, we have one more zero to spare
                    k += 1
                left += 1

            right += 1

        return right - left
