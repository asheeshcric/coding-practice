"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in
the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights
associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum
value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. 
You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
"""


def knapsack(weights, values, W, n):
    # Use the array "dp" for memoization
    global dp
    # Base case: Either all items are finished or the capacity of knapsack is reached
    if n <= 0 or W <= 0:
        return 0

    # If the value is already calculated, use it
    if dp[n][W] != -1:
        return dp[n][W]

    # Check if the weight of the item is under the capacity of knapsack
    if weights[n-1] <= W:
        # If the item's weight is smaller than the remaining capacity of the knapsack,
        # then we have two options: either to include the item or to not include it
        # Since we want to maximize the weights, we choose the max between the two
        # Also, to optimize the code, we use memoization and store the intermediate values in an array
        # To determine the size of the memoized array, just look at the variables that are changing during the
        # recursive calls (W and n in this case)
        dp[n][W] = max(
            weights[n-1] + knapsack(weights, values, W-weights[n-1], n-1),
            knapsack(weights, values, W, n-1)
        )
    else:
        dp[n][W] = knapsack(weights, values, W, n-1)

    return dp[n][W]


if __name__ == '__main__':
    weights = [10, 20, 30]
    values = [60, 100, 120]
    W = 50
    # When initializing an array for memoization, always take its size larger than actually required
    # This prevents indexing errors
    dp = [[-1 for i in range(W+1)] for j in range(len(weights)+1)]
    # print(len(dp), len(dp[0])
    print(knapsack(weights, values, W, len(weights)))
