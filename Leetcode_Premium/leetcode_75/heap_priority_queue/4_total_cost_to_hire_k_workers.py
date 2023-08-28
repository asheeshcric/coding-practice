"""
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost 
from either the first candidates workers or the last candidates workers. 
Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, 
then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker 
because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. 
Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.
"""
from typing import List
from heapq import heapify, heappop, heappush
from collections import deque


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Since a person can be hired from two sets of candidates (left_set, right_set)
        lr_pairs = []
        right_set_idx = max(candidates, len(costs) - candidates)
        remaining = deque([])
        for i, cost in enumerate(costs):
            if i < candidates:
                # Left set of candidates
                lr_pairs.append((cost, "left"))
            elif i >= right_set_idx:
                # Right set of candidates
                lr_pairs.append((cost, "right"))
            else:
                # Those didn't make as candidates
                remaining.append(cost)

        total_costs = 0
        heapify(lr_pairs)
        # We need k workers
        for _ in range(k):
            cost, side = heappop(lr_pairs)
            total_costs += cost
            if remaining:
                # Once, a candidate is hired from a set, add one of the remaining candidates
                # to the left or the right set depending on where the last one was hired from
                if side == "left":
                    # Add any remaining candidate to the left set
                    heappush(lr_pairs, (remaining.popleft(), "left"))
                else:
                    heappush(lr_pairs, (remaining.pop(), "right"))

        return total_costs
