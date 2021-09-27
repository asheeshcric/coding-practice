"""
Solve this problem like a merge sort problem

Base Cases:
    a. If no buildings: return an empty list
    b. If only one building: return the top-left and bottom-right corners of the building <== [[Li, Hi], [Ri, 0]]

All other cases:
    a. Get the leftSkyline (first n/2 buildings)
    b. Get the rightSkyline (last n/2 buildings)
    c. Merge both the lists

Merging skylines:
1. The height of an output skyline is always a maximum between the left and the right skylines
2. pL and pR as pointers to track the current coordinate index in both left and right skylines
    - leftY, rightY, and currY to track the current height of the left, right and the merged skylines
3. When in the region where left and right skylines overlap:
    a. Pick up the smallest x-coordinate
        - If it is from the left skyline, pL += 1 and update leftY
        - Else pR += 1 and update rightY
    b. Compute the largest height at the current point: maxY = max(leftY, rightY)
    c. Add (x, maxY) to the output if maxY != currY (this means we encountered the next coordinate at a different height)

4. Repeat until both left and right skylines are completely processed.
"""

from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Base cases
        if not buildings:
            return []
        if len(buildings) == 1:
            L, R, H = buildings[0]
            return [[L, H], [R, 0]]

        # Normal case
        n = len(buildings)
        left_skyline = self.getSkyline(buildings[: n // 2])
        right_skyline = self.getSkyline(buildings[n // 2 :])

        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left, right):
        def update_output(x, y):
            """
            Update the final output with the new element.
            """
            # if skyline change is not vertical -
            # add the new point
            if not output or output[-1][0] != x:
                output.append([x, y])
            # if skyline change is vertical -
            # update the last point
            else:
                output[-1][1] = y

        def append_skyline(p, lst, n, y, curr_y):
            """
            Append the rest of the skyline elements with indice (p, n)
            to the final output.
            """
            while p < n:
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y

        n_l, n_r = len(left), len(right)
        p_l = p_r = 0
        curr_y = left_y = right_y = 0
        output = []

        # while we're in the region where both skylines are present
        while p_l < n_l and p_r < n_r:
            point_l, point_r = left[p_l], right[p_r]
            # pick up the smallest x
            if point_l[0] < point_r[0]:
                x, left_y = point_l
                p_l += 1
            else:
                x, right_y = point_r
                p_r += 1
            # max height (i.e. y) between both skylines
            max_y = max(left_y, right_y)
            # if there is a skyline change
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y

        # there is only left skyline
        append_skyline(p_l, left, n_l, left_y, curr_y)

        # there is only right skyline
        append_skyline(p_r, right, n_r, right_y, curr_y)

        return output
