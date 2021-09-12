"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i, num in enumerate(nums):
            if num != 0:
                continue

            k = i + 1
            while k < len(nums) and nums[k] == 0:
                k += 1

            if k == len(nums):
                # This means we encountered all zeroes after index i. So, we don't need to change anything
                break

            # Swap that element with the current zero
            nums[i], nums[k] = nums[k], nums[i]
            if not any(nums[k:]):
                # This means there aren't any non-zero integers left to be swapped
                break
