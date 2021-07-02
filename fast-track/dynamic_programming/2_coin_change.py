"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Solution:

1. First, fill up the dp table with a value just greater than the required amount. Since, the minimum number of coins to reach amount 11 would be 11 if we only have 1 as
the coin denomination 
2. Each index in the dp table represents a sub-amount and the value at that index represents the minimum number of coins needed to obtain that amount.
3. So, we start from the 0th index (requiring 0 coins) and move forward
    - For each index (or subamount), we try to fill it with every coin that we have and replace the value at that index with the minimum number of coins that successfully
    reached the amount.
4. We keep on repeating this process until we reach the end of the dp array. Finally, we get our solution at the end of the array.

"""


def coin_change(coins, amount):
    # First fill in the dp table with a value greater than the required amount
    dp = [amount + 1 for _ in range(amount + 1)]
    # For amount 0, the number of coins required is 0
    dp[0] = 0
    print(dp)
    for i in range(1, len(dp)):
        for coin in coins:
            if i - coin >= 0:
                # If only selecting that coin is valid for that amount
                dp[i] = min(dp[i - coin] + 1, dp[i])

    print(dp)
    return dp[amount]


if __name__ == "__main__":
    print(coin_change([1, 2, 5], 11))
