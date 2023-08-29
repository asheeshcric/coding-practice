"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

"""
from typing import List

"""
We start from the last step by adding the cost at the top of the ladder as 0.

1. At last step, there is only one option: One jump to the top. Hence, it already has the 
min cost to reach the top, i.e. cost[-1] + 0

2. Hence, we start moving backwards in the list from the second last step:
    - For that step, we have two options: One-step jump or Two-step jump
    - Find the min cost among the two: cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])

3. Finally, return the min cost at step 0 or 1.
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Add the cost of being on top the ladder as 0
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            # We start from the second last step (since the last one will always remain with min cost (one jump))
            cost[i] = min(cost[i] + cost[i + 1], cost[i] + cost[i + 2])

        return min(cost[0], cost[1])
