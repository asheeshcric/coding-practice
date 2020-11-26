"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with
sum equal to given sum.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.


Code: I used the same 0-1 knapsack solution and compared the final value with the target. If both are equal,
then return True, else return False
"""


def subset_sum(numbers, target, n):
    """
    Recursive approach
    """
    if n == 0 or target == 0:
        return 0

    if numbers[n-1] <= target:
        return max(
            numbers[n-1] + subset_sum(numbers, target-numbers[n-1], n-1),
            subset_sum(numbers, target, n-1)
        )
    else:
        return subset_sum(numbers, target, n-1)


def subset_sum_bottom_up(numbers, target, n):
    dp = [[False for col in range(target+1)] for row in range(n+1)]

    if target == 0:
        return True

    if n == 0:
        return False

    for i in range(n+1):
        for j in range(target+1):
            if i == 0:
                dp[i][j] = False
            elif j == 0:
                dp[i][j] = True
            else:
                if numbers[i-1] <= target:
                    dp[i][j] = dp[i-1][j-numbers[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[n][target]



if __name__ == '__main__':
    numbers = [3, 34, 4, 12, 5, 2]
    target = 30
    n = len(numbers)
    # Recursive way
    max_sum = subset_sum(numbers, target, n)
    if max_sum == target:
        print(True)
    else:
        print(False)

    target = 9
    # Bottom-up approach
    print(subset_sum_bottom_up(numbers, target, n))
