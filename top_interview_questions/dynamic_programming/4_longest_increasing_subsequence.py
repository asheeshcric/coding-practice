from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        dp = [1 for _ in range(len(nums))]

        for j in range(1, len(nums)):
            for i in range(j):
                if dp[j] > dp[i]:
                    dp[j] = max(1 + dp[i], dp[j])

        return dp[-1]
