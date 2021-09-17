from typing import List


class Solution:
    def merge_overlap(self, int1, int2):
        if int1[0] > int2[0]:
            int1, int2 = int2, int1

        # Check if they overlap or not
        if int1[1] < int2[1]:
            # Do not overlap
            return None
        else:
            return [int1[0], max(int1[1], int2[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # First sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for int2 in intervals[1:]:
            int1 = output[-1]
            overlap = self.merge_overlap(int1, int2)
            if overlap:
                output[-1] = overlap
            else:
                output.append(int2)

        return output
