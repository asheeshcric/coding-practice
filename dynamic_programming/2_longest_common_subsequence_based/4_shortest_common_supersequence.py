"""
Given two strings str1 and str2, the task is to find the length of the shortest string that has both 
str1 and str2 as subsequences.

Examples : 

Input:   str1 = "geek",  str2 = "eke"
Output: 5
Explanation: 
String "geeke" has both string "geek" 
and "eke" as subsequences.

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  9
Explanation: 
String "AGXGTXAYB" has both string 
"AGGTAB" and "GXTXAYB" as subsequences
"""


def scs(x, y, n, m):
    global dp

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                if x[i-1] == y[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Now we have the length of LCS
    # Because we can write the LCS only once from both string, just subtract the len of LCS
    return n + m - dp[n][m]


if __name__ == '__main__':
    x = 'ABCDGH'
    y = 'AEDFHR'
    x, y = x.lower(), y.lower()
    n, m = len(x), len(y)
    dp = [[None for col in range(m+1)] for row in range(n+1)]
    # A supersequence has LCS between two strings that is only written once.
    # So if we know the length of LCS, we can find the length of Supersequence using the length of the longer
    # string
    print(scs(x, y, n, m))
