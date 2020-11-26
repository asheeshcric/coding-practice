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
    if n == 0 or target == 0:
        return 0

    if numbers[n-1] <= target:
        return max(
            numbers[n-1] + subset_sum(numbers, target-numbers[n-1], n-1),
            subset_sum(numbers, target, n-1)
        )
    else:
        return subset_sum(numbers, target, n-1)


if __name__ == '__main__':
    numbers = [3, 34, 4, 12, 5, 2]
    target = 30
    n = len(numbers)
    max_sum = subset_sum(numbers, target, n)
    if max_sum == target:
        print(True)
    else:
        print(False)
