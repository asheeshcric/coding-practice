"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.


Solution: This is similar to the unbounded knapsack 0-1 problem. Using a 2D dp matrix, we track for both different coins and different amounts
"""


def num_combinations(amount, coins, n):
    # Base case
    if amount == 0:
        return 1

    if n == 0 or amount < 0:
        return 0

    # Check if the coin denomination is less than the required remaining amount
    # If we select the coin, we can again select the same coin in the next step
    # If we don't select the coin, we don't go back to that coin again
    if coins[n - 1] <= amount:
        return num_combinations(amount - coins[n - 1], coins, n) + num_combinations(
            amount, coins, n - 1
        )
    else:
        # We don't select the coin
        return num_combinations(amount, coins, n - 1)


if __name__ == "__main__":
    amount, coins = 5, [1, 2, 5]
    print(num_combinations(amount, coins, len(coins)))
