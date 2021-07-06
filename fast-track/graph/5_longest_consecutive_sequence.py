"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


def longest_cons_sequence(nums):
    nums = set(nums)
    max_length = 1
    for num in nums:
        current_length = 1
        if num - 1 not in nums:
            # num is the start of a sequence
            while num + 1 in nums:
                current_length += 1
                num = num + 1
            max_length = max(max_length, current_length)

    return max_length


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(longest_cons_sequence(nums))
