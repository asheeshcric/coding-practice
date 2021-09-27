from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack will contain tuples of (idx, temp)
        # Also, the stack is a monotonic non-decreasing stack
        stack = []
        answer = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            # When the current temp > temp at the top of the stack,
            # Pop it from the stack and add the number of days for that idx in the answer list
            while stack and temp > stack[-1][1]:
                idx, tempx = stack.pop()
                answer[idx] = i - idx

            stack.append((i, temp))

        return answer
