"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Solution:
1. Start from the first number and check if it is the start of a new sequence
    - If it is, check for all consecutive numbers and record the length (comparing to the max length)
    - If it is not, ignore it (you will get back to it from the start of another sequence)
2. At the end, the longest sequence length will be recorded.
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
