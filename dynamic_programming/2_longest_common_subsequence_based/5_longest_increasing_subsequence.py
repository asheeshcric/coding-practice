"""
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given
sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS
for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

"""


def lis(A, n):
    global dp

    if n == 0 or n == 1:
        return n

    # Add memoization to speed up
    if dp[n] is not None:
        return dp[n]

    if A[n-2] <= A[n-1]:
        dp[n] = max(1+lis(A, n-1), lis(A, n-1))
    else:
        dp[n] = lis(A, n-1)

    return dp[n]


if __name__ == '__main__':
    A = [3, 10, 2, 1, 20]
    dp = [None]*(len(A)+1)
    print(lis(A, len(A)))
