"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


def three_sum(nums):
    n = len(nums)
    if n < 3:
        return []

    nums = sorted(nums)
    triplets = set()
    for i in range(0, n - 2):
        j, k = i + 1, n - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == 0:
                triplet = (nums[i], nums[j], nums[k])
                triplets.add(triplet)
                j += 1
                k -= 1
            elif s < 0 and nums[j] < nums[k]:
                j += 1
            else:
                k -= 1

    return [list(triplet) for triplet in triplets]


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))
