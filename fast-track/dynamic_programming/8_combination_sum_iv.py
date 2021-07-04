"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Similar to unbounded knapsack or coin change problem, but here sequence also matters. We will need to keep track of the sequence too,
i.e 1+2+1 and 2+1+1 and 1+1+2 are three different sequences


Solution:
1. Construct a dp array that will contain number of combinations for each target from 1 to target. Initialize with 0, except dp[0] = 1 (one way for 1 number, base case)
2. Now for each target with index i (=1, target):
    - for each number in nums, decrease that number from the target and see how many combinations were previously formed. Add that to the current target
    - Keep doing this for each number for each target
3. The final will have all combinations for the given numbers and the target
"""


def combination_sum(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: 1 number can be combined in 1 ways
    for i in range(1, target + 1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i - num]

    return dp[target]


if __name__ == "__main__":
    nums = [1, 2, 3]
    target = 4
    print(combination_sum(nums, target))
