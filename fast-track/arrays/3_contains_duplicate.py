"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(contains_duplicate(nums))
