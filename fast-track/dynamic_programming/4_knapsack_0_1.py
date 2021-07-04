def knapsack(weights, values, C, n, dp):
    # Recursive approach with memoization technique

    # Base case: Either we are out of items or we don't have space left in the knapsack
    if n <= 0 or C <= 0:
        return 0

    # Check if max profit has already been calculated for this capacity
    if dp[n][C] != -1:
        return dp[n][C]

    # Check if the current item fits in the knapsack or not
    if weights[n - 1] <= C:
        # Two options: Either include it or not
        # Select whichever gives the maximum value (profit)
        dp[n][C] = max(
            values[n - 1] + knapsack(weights, values, C - weights[n - 1], n - 1, dp),
            knapsack(weights, values, C, n - 1, dp),
        )
    else:
        # The item cannot be fit in the knapsack
        dp[n][C] = knapsack(weights, values, C, n - 1, dp)

    return dp[n][C]


if __name__ == "__main__":
    weights = [3, 5, 2]
    values = [1, 3, 3]
    C = 5
    # To add memoization: construct a dp matrix for each capacity weight of the knapsack vs the number of items (indices)
    dp = [[-1 for _ in range(C + 1)] for z in range(len(weights) + 1)]
    print(knapsack(weights, values, C, len(weights), dp))
