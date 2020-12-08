"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

"""
import math


def count_subsets(numbers, target, n):
    if target == 0:
        return 1
    if n == 0:
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
                if numbers[i-1] <= j:
                    dp[i][j] = dp[i-1][j-numbers[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[n][target]


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    output_sum = 3

    # First find the target that needs to be achieved
    # The given output_sum is the difference between two subsets S1 and S2
    # S1 would contain all '+' signed numbers and S2 would contain all '-' signed numbers
    # Now, we need to count the number of subsets that equal the sum to the calculated target value
    target = math.ceil((sum(numbers)+output_sum)/2)
    print(count_subsets(numbers, target, n=len(numbers)))
