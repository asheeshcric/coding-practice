"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Solution: Similar to knapsack 0-1 problem with different constraints
"""


def max_money(nums, n, dp):
    if n <= 0:
        return 0

    if dp[n] is not None:
        return dp[n]

    dp[n] = max(nums[n - 1] + max_money(nums, n - 2, dp), max_money(nums, n - 1, dp))
    return dp[n]


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    dp = [None] * (len(nums) + 1)
    print(max_money(nums, len(nums), dp))
