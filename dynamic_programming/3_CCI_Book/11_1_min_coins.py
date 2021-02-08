"""
Given a denominations of coins such as [25, 10, 5, 1], find the minimum number these coins required
to make "n" cents
"""


def num_ways(amount, denoms, dp):
    if amount == 0:
        return 0

    dp[0] = 0

    for i in range(1, len(dp)):
        for denom in denoms:
            if denom <= i:
                dp[i] = min(1+dp[i-denom], dp[i])

    return -1 if dp[amount] > amount else dp[amount]


def coins(n):
    dp = [n+1]*(n+1)
    denoms = [25, 10, 5, 1]
    return num_ways(n, denoms, dp)


print(coins(3))
