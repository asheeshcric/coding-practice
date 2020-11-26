"""
Given an array arr[] of length N and an integer X, the task is to find the number of subsets with sum equal to X.

Input: arr[] = {1, 2, 3, 3}, X = 6
Output: 3
All the possible subsets are {1, 2, 3},
{1, 2, 3} and {3, 3}

Input: arr[] = {1, 1, 1, 1}, X = 1
Output: 4
"""

import time


def c_recursion(numbers, target, n):
    global dp
    if n < 0:
        return 0

    if target == 0:
        return 1

    # Memoization
    if dp[n][target] is not None:
        return dp[n][target]

    if numbers[n-1] <= target:
        dp[n][target] = c_recursion(numbers, target-numbers[n-1], n-1) + c_recursion(numbers, target, n-1)
    else:
        dp[n][target] = c_recursion(numbers, target, n-1)

    return dp[n][target]


def count_subset_sum(numbers, target, n):
    if target == 0 or n == 0:
        return 0

    dp = [[0 for col in range(target+1)] for row in range(n+1)]

    for i in range(n+1):
        for j in range(target+1):
            if i == 0 or j == 0:
                if i == 0:
                    dp[i][j] = 0
                if j == 0:
                    dp[i][j] = 1

            else:
                if numbers[i-1] <= target:
                    dp[i][j] = dp[i-1][j-numbers[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[n][target]


if __name__ == '__main__':
    numbers = [1, 2, 3, 3]
    target = 6
    n = len(numbers)
    dp = [[None for col in range(target+1)] for row in range(n+1)]
    start_time = time.time()
    print(count_subset_sum(numbers, target, n))
    print(time.time()-start_time)
    start_time = time.time()
    print(c_recursion(numbers, target, n))
    print(time.time()-start_time)
