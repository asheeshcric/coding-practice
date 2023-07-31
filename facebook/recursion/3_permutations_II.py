from typing import List
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

    def permute(self, nums):
        # Base case
        if len(nums) == 1:
            return [nums[:]]

        result = []
        for i in range(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                # Encountered a duplicate number, so no need to permute this
                continue

            
