"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_optimized(nums, target):
    # Use a dictionary to store seen numbers and their indices
    seen = dict()
    for i, num in enumerate(nums):
        if (target - num) in seen:
            return [seen[target - num], i]
        else:
            seen[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
    print(two_sum_optimized(nums, target))
