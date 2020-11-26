"""
Partition problem is to determine whether a given set can be partitioned into two subsets
such that the sum of elements in both subsets is the same. 

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.
"""


def subset_sum(numbers, target, n):
    # Same as last problem
    dp = [[False for col in range(target+1)] for row in range(n+1)]

    if target == 0 or n == 0:
        # Case when there are not elements in the array
        return False

    else:
        for i in range(n+1):
            for j in range(target+1):
                # Initialization: if target is 0, empty subset is possible (so True for all i=0)
                # If len(numbers)=0, then no subset can be formed to sum up to a target (so False for all j=0)
                if i == 0:
                    dp[i][j] = False
                    continue
                if j == 0:
                    dp[i][j] = True
                    continue

                if numbers[i-1] <= target:
                    dp[i][j] = dp[i-1][j-numbers[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

    return dp[n][target]


def has_equal_partition(numbers):
    n = len(numbers)
    total = sum(numbers)
    # Check if the total sum of the numbers is odd or not: if odd --> equal partition is not possible
    if total % 2 == 1:
        return False
    else:
        return subset_sum(numbers, int(total/2), n)


if __name__ == '__main__':
    numbers = [1, 5, 11, 5]
    print(has_equal_partition(numbers))
