"""
Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.


Refer to 1_longest_common_subsequence to understand the concept behind this bottom up approach
"""


def print_lcs(x, y, n, m):
    global dp

    # Initialize the matrix at i=0 or j=0
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = ''

            else:
                if x[i-1] == y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + x[i-1]
                else:
                    # Choose the one that has the max length
                    if len(dp[i-1][j]) > len(dp[i][j-1]):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1]

    return dp[n][m]


if __name__ == '__main__':
    x = 'geeks'
    y = 'gekkms'
    n, m = len(x), len(y)
    dp = [[None for col in range(m+1)] for row in range(n+1)]
    print(print_lcs(x.lower(), y.lower(), n, m))
    print(dp)
