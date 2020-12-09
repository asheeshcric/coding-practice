"""
Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.

Input : X = “GeeksforGeeks”, y = “GeeksQuiz”
Output : 5
The longest common substring is “Geeks” and is of length 5.

"""


def lcs_recursive(x, y, n, m, count=0):
    # Base condition
    if n == 0 or m == 0:
        return count

    if x[n-1] == y[m-1]:
        count = lcs_recursive(x, y, n-1, m-1, count+1)

    count = max(count, max(lcs_recursive(x, y, n-1, m),
                           lcs_recursive(x, y, n, m-1)))

    return count


def lc_substring(x, y, n, m):
    global dp

    max_len = 0

    # Initialize the matrix
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                dp[i][j] = 0

            else:
                if x[i-1] == y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    # Track the substring with max length
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0

    return max_len


if __name__ == '__main__':
    x = 'GeeksforGeeks'
    y = 'GeeksQuiz'
    x, y = x.lower(), y.lower()
    n, m = len(x), len(y)
    dp = [[None for col in range(m+1)] for row in range(n+1)]
    # Using the bottom up approach
    print(lc_substring(x, y, n, m))
    # Recursive approach
    print(lcs_recursive(x, y, n, m))
