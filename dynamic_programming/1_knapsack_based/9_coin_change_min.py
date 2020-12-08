"""
Given a value V, if we want to make change for V cents, and we have infinite supply of each of 
C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?
Examples:

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents 

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents

"""


def min_coins(coins, target):
    n = len(coins)
    dp = [[0 for col in range(target+1)] for row in range(n+1)]

    # First initialize the first row and column
    for i in range(n+1):
        for j in range(target+1):
            if i == 0 or j == 0:
                if i == 0:
                    dp[i][j] = j
                if j == 0:
                    dp[i][j] = 0
            else:
                if coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])

    return dp


if __name__ == '__main__':
    coins = [9, 6, 5, 1]
    target = 11
    dp = min_coins(coins, target)
    print(dp[len(coins)][target])
    # Trace back the coins that add up to the target sum
    traced_coins = []
    # Start from the last cell (i.e. row=n and col=target)
    row, col = len(coins), target
    try:
        while sum(coins) != target:
            if dp[row][col] == dp[row-1][col]:
                row -= 1
                continue
            else:
                traced_coins.append(coins[row-1])
                # Move to next column as follows
                col = col - coins[row-1]
    except Exception as error:
        print(error)
        print(row, col)
