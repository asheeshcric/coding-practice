"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
Return 0 if there is no such subarray.

"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Similar to the max consecutive ones III problem, but here k=1 is fixed since we're deleting only one element
        # Also, at the end, since one element is removed we need to subtract that from the length of the resulting subarray
        k = 1
        left, right = 0, 0
        while right < len(nums):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                # This means we've already deleted one 0, Hence, move left side of the window
                if nums[left] == 0:
                    k += 1

                left += 1

            right += 1

        # Since we must delete one element from the list, the final subarray will have one less item (with deleted 0 or 1)
        return right - left - 1
