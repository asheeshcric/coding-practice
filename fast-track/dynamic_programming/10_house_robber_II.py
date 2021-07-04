"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
"""


def max_money(nums, n, dp):
    if n <= 0:
        return 0

    if dp[n] is not None:
        return dp[n]

    dp[n] = max(nums[n - 1] + max_money(nums, n - 2, dp), max_money(nums, n - 1, dp))
    return dp[n]


if __name__ == "__main__":
    # Same as house_robber problem, now just need to compared between [0:last-1] and [1:last]
    nums = [1, 2, 3, 1]
    dp1 = [None] * (len(nums))
    dp2 = [None] * (len(nums))
    ans = max(
        max_money(nums[1:], len(nums) - 1, dp1),
        max_money(nums[:-1], len(nums) - 1, dp2),
    )
    print(ans)
