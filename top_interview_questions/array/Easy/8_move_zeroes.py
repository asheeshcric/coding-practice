"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

U:
- Return the same list by moving all the zeroes to the end
- The order of other numbers should not change, and all number (except for zero) should be on the left side of the list
- Should we traverse from the left side or the right side?
M:
- Traversing a list with two pointers

P:
- Whenever we encounter a zero, we swap it with the next non-zero item in the list
- So, we use two pointers: One points to the current index in the list and the other moves faster that finds the next non-zero number

I:
- i and j point to 1st and 2nd element in the list
- if nums[i] == 0:
    - we need to swap it with the next non-zero number
    - j tracks where the next non-zero number is
    - When j finds it, we swap the numbers
    - Then, we move both i and j one step to the right

- if at any time, j goes out of bounds, i.e. j >= len(nums), we know that we don't have any non-zero numbers left to swap
- So, we break the loop and stop

"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return

        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] == 0:
                # Need to replace this 0 with a non-zero number if exists
                while j < len(nums) and nums[j] == 0:
                    j += 1

                if j >= len(nums):
                    break

                # Swap 0 with the next non-zero number
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
