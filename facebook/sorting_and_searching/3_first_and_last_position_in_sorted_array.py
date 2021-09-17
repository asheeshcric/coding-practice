from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = self.bin_search(nums, target, left_side=True)
        right_idx = self.bin_search(nums, target, left_side=False)
        return [left_idx, right_idx]

    def bin_search(self, nums, target, left_side=True):
        left, right = 0, len(nums)-1
        idx = -1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                idx = mid
                if left_side:
                    # Go to the left portion of the current mid
                    right = mid - 1
                else:
                    left = mid + 1

        return idx
