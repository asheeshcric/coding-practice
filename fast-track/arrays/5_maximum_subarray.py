"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""


def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    nums = [-2, 2, 5, -11, 6]
    print(max_subarray(nums))
