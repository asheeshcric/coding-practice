"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, 
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a is not None and a < 0 and stack[-1] > 0:
                # The above condition guarantees a collsion.
                # Now, see which one gets destroyed
                diff = a + stack[-1]
                if diff > 0:
                    # This means the negative asteroid (a) gets destroyed, so we don't do anything to the stack
                    a = None
                elif diff < 0:
                    # This means the positive asteroid on top of the stack gets destroyed
                    stack.pop()
                else:
                    # Both get destroyed
                    a = None
                    stack.pop()

            if a is not None:
                stack.append(a)

        return stack
