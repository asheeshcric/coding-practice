from typing import List


"""
Use binary search: for each mid point, check if the target is in the left sorted region or the right sorted region
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            # Check if we are in the left sorted position in the array
            if nums[left] <= nums[mid]:
                # Now, check if target lies in that left portion or the right portion
                if target > nums[mid] or target < nums[left]:
                    # This means the target lies in the right portion
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # We are in the right sorted portion of the array
                if target < nums[mid] or target > nums[right]:
                    # This means the target lies in the left portion
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
