from typing import List

"""
- For amount 0, we know that we need 0 coins
- Starting from amount = 1 to total_amount, for each amount:
    - Find min number of coins required
        - We can add one coin to one of the previous amounts, or we can directly get a coin equal to that amount

- At the end, when we reach the total_amount, we will get the min number of coins required

"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]
        # Since we would require 0 coins for an amount of 0
        dp[0] = 0

        for curr_amount in range(1, amount + 1):
            for coin in coins:
                # First check if the coin we are selecting is less than or equal to the amount that we want to make
                if curr_amount - coin >= 0:
                    dp[curr_amount] = min(1 + dp[curr_amount - coin], dp[curr_amount])

        return dp[amount] if dp[amount] != float("inf") else -1
