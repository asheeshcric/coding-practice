"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""


def max_product_subarray(nums):
    current_max, current_min = nums[0], nums[0]
    max_prod = nums[0]
    for i in range(1, len(nums)):
        temp = current_max * nums[i]
        current_max = max(nums[i], nums[i] * current_max, nums[i] * current_min)
        current_min = min(nums[i], temp, nums[i] * current_min)
        max_prod = max(max_prod, current_min, current_max)

    return max_prod


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(max_product_subarray(nums))
