"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

1. Set the last index of the array as the goal to reach
2. Start from the second last index (moving all the way to the left one at a time)
    - Check if you can reach the current goal from that index, by adding the number at that position to the index value
    - If you can, update the goal

3. Once you go through all the indices, check if your goal has shifted from the end to the first element in the array
    - If yes, return True
    - Else, return False
"""


def can_jump(nums):
    goal = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    if goal == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(can_jump(nums))
