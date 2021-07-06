"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, 
such that the container contains the most water.

Notice that you may not slant the container.
"""


def most_water(height):
    max_width = len(height) - 1
    left, right = 0, max_width
    max_area = 0
    for width in range(max_width, 0, -1):
        if height[left] < height[right]:
            max_area = max(max_area, width * height[left])
            left = left + 1

        else:
            max_area = max(max_area, width * height[right])
            right = right - 1

    return max_area


if __name__ == "__main__":
    height = [4, 3, 2, 1, 4]
    print(most_water(height))
