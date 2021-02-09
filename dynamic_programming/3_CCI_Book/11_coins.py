from typing import List

def change(amount: int, coins: List[int]) -> int:
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for denom in coins:
        for total in range(1, amount + 1):
            if total >= denom:
                dp[total] += dp[total - denom]
    return dp[amount]


print(change(5, [1, 2, 3]))
