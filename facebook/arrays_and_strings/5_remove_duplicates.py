from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums < 2:
            return len_nums

        new_i, old_i = 1, 1

        while old_i < len(nums):
            if nums[old_i] == nums[old_i-1]:
                # Found a duplicate number
                old_i += 1
                continue

            nums[new_i] = nums[old_i]
            new_i += 1
            old_i += 1

        return new_i
