"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Solution:
    1. Construct a dp array that is initialized with 1 for all elements in the array
        - This means we can atleast draw one LIS from the array
    2. You will need to use two pointers in the dp array
        - "i" goes through each element of the array one by one
        - "j" keeps track of the elements before

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


if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    dp = [1 for _ in arr]
    print(LIS(arr, dp))
