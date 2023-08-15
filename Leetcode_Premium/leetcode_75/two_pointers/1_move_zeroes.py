"""
Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start, stop = 0, 1
        while start < len(nums) and stop < len(nums):
            # Check for the first zero
            if nums[start] == 0:
                # Move the stop pointer until you find a non-zero number to replace
                # the current zero at start
                while stop < len(nums) and nums[stop] == 0:
                    stop += 1

                if stop >= len(nums):
                    # This means the rest of the array is all zeroes, so we stop
                    break

                # Else, we replace the current zero with the non-zero number
                nums[start], nums[stop] = nums[stop], nums[start]

            start += 1
            stop += 1
