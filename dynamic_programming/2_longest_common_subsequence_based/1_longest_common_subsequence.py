"""
Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence 
that appears in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""


def lcs(x, y, n, m):
    global dp
    # Base condition
    if n == 0 or m == 0:
        return 0

    # Memoization of the calculations
    if dp[n][m] is not None:
        return dp[n][m]

    # First check if the last chars match in both strings
    if x[n-1] == y[m-1]:
        dp[n][m] = 1 + lcs(x, y, n-1, m-1)

    else:
        # Select the one with max LCS
        dp[n][m] = max(lcs(x, y, n-1, m), lcs(x, y, n, m-1))

    return dp[n][m]


def lcs_bottom_up(x, y, n, m):
    global dp

    # Initialize the dp matrix
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                if x[i-1] == y[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]


if __name__ == '__main__':
    x = 'ABCDGH'
    y = 'AEDFHR'
    n, m = len(x), len(y)
    dp = [[None for col in range(m+1)] for row in range(n+1)]
    print(lcs(x.lower(), y.lower(), n, m))
    print(lcs_bottom_up(x.lower(), y.lower(), n, m))
