"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""


def min_rotated_array(nums):
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        midpoint = int(left + (right - left) / 2)
        if midpoint > 0 and nums[midpoint] < nums[midpoint - 1]:
            return nums[midpoint]
        elif nums[left] <= nums[midpoint] and nums[right] <= nums[midpoint]:
            # This means the left half is properly sorted, so we focus on the right half
            left = midpoint + 1
        else:
            # This means the right half is properly sorted, so we focus on the left half
            right = midpoint - 1

    return nums[left]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(min_rotated_array(nums))
