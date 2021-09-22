from typing import List

"""
Understand (U):
    - First, move all unique values to the front of the list without changing their order
    - Return the index up to which the array contains all unique values
Match (M): A two pointer approach: 
Plan (P):
    - First points to the index where we want to place the number
    - Second traverses through the whole list one at a time
    - Check if two numbers are duplicates, if yes: move the second pointer else: move both the pointers
Implement (I):
Review (R):
[0, 0, 1, 1, 2, 2, 3, 4] ==> [0, 1, 2, 3, 4, ...]

"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                # Duplicate found: move the j pointer ahead
                j += 1
            else:
                # A new unique value is detected. Need to place it at i+1
                nums[i + 1] = nums[j]
                i += 1
                j += 1

        return i+1
