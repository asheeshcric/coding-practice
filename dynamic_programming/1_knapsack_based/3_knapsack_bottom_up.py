"""
Here, a (n+1)x(capacity+1) matrix if created and the first row and first column are initialized to 0
0 0 0 0 ... 0
0
0
.
.
.
0
NOTE: rows = (number_of_items+1) and columns = (capacity+1)
So, each cell (i,j) in the matrix gets filled by the maximum value possible for the corresponding capacty and the number
of items 
"""


def knapsack(weights, values, capacity, n):
    # Initialize a storage matrix for dynamic programming
    dp = [[0 for col in range(capacity+1)] for row in range(n+1)]

    for i in range(n+1):
        for j in range(capacity+1):
            if i == 0 or j == 0:
                # If either no item is present or the capacity of the knapsack is zero,
                # then the max value possible is 0
                dp[i][j] = 0
            else:
                # First check if the item's weight can be added to the sack
                if weights[i-1] <= capacity:
                    dp[i][j] = max(
                        values[i-1]+dp[i-1][j-weights[i-1]],
                        dp[i-1][j]
                    )
                else:
                    # Ignore the current weight and move on to the next one
                    dp[i][j] = dp[i-1][j]

    return dp[n][capacity]


if __name__ == '__main__':
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    print(knapsack(weights, values, capacity, len(values)))
