from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum, max_sum = nums[0], nums[0]
        for num in nums[1:]:
            # Disregard previous sum if it negatively adds to the current number
            curr_sum = max(num, curr_sum + num)
            # Update the max_sum
            max_sum = max(max_sum, curr_sum)

        return max_sum
