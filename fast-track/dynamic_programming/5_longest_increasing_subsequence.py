"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Solution:
    1. Construct a dp array that is initialized with 1 for all elements in the array
        - This means we can atleast draw one LIS from the array
    2. You will need to use two pointers in the dp array
        - "j" starts from the second element and goes to the end
        - "i" moves from 0th index until j-1 and compares the values with value at "j"
        - if arr[j] > arr[i], it means the subsequence can be increased by 1 for all the previous subsequences of length i

"""


def LIS(arr, dp):
    if len(arr) <= 0:
        return 0

    if len(arr) == 1:
        return 1

    for j in range(1, len(arr)):
        for i in range(j):
            if arr[j] > arr[i]:
                dp[j] = max(1 + dp[i], dp[j])
    print(dp)
    return max(dp)


def LIS_II(arr, dp):
    # Idea is to start checking from the end
    # For each index, there will only be 1
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    dp = [1 for _ in arr]
    print(LIS(arr, list(dp)))
    print(LIS_II(arr, dp))
