"""
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference 
between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and
the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11 
"""


def max_sum_knapsack(numbers, target, n):
    if n == 0 or target == 0:
        return 0

    if numbers[n-1] <= target:
        return max(
            numbers[n-1] + max_sum_knapsack(numbers, target-numbers[n-1], n-1),
            max_sum_knapsack(numbers, target, n-1)
        )
    else:
        return max_sum_knapsack(numbers, target, n-1)


def max_sum_bottom_up(numbers, target, n):
    if n == 0 or target == 0:
        return 0

    dp = [[0 for col in range(target+1)] for row in range(n+1)]
    for i in range(n+1):
        for j in range(target+1):
            if i == 0 or j == 0:
                dp[i][j] = 0

            else:
                if numbers[i-1] <= target:
                    dp[i][j] = max(
                        numbers[i-1]+dp[i-1][j-numbers[i-1]],
                        dp[i-1][j]
                    )
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[n][target]


if __name__ == '__main__':
    numbers = [1, 6, 100, 5]
    n = len(numbers)
    target = int(sum(numbers)/2)
    target = target+1 if sum(numbers) % 2 == 1 else target
    max_sum = max_sum_bottom_up(numbers, target, n)
    print(max_sum)
    result = abs(sum(numbers)-max_sum*2)
    print(result)
