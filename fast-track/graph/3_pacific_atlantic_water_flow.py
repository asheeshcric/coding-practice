"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells.
You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west
if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans

Discussion:

1. Pacific Ocean is on the top and left of the matrix. So, the first row and the first column touches the Pacific ocean
2. Atlantic ocean is to the right and bottom of the matrix. So, the last column and the last row touch the Atlantic ocean
3. We start from all four edges of the matrix and move inwards only if the next height is greater than the current height
4. We will keep track of the cells that can flow to both pacific and atlantic oceans separately
5. After we're done, we will merge both the sets and find intersection of them to find out the cells that can flow to both oceans

"""


def pacific_atlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    visit_pac, visit_atl = set(), set()

    def dfs(r, c, visit, previous_height):
        # Need to check if it has already been visited or (r, c) is out of bounds or the current height is less than the previous height or not
        if (
            (r, c) in visit
            or r < 0
            or c < 0
            or r >= ROWS
            or c >= COLS
            or heights[r][c] < previous_height
        ):
            # This cell cannot flow to the oceans
            return

        visit.add((r, c))
        # Do DFS on all four sides of the current cell
        dfs(r + 1, c, visit, previous_height=heights[r][c])
        dfs(r - 1, c, visit, previous_height=heights[r][c])
        dfs(r, c + 1, visit, previous_height=heights[r][c])
        dfs(r, c - 1, visit, previous_height=heights[r][c])

        return visit

    # When visiting first row and last row
    for c in range(COLS):
        # DFS for first row for pacific
        visit_pac = dfs(0, c, visit_pac, heights[0][c])
        # DFS for last row for atlantic
        visit_atl = dfs(ROWS - 1, c, visit_atl, heights[ROWS - 1][c])

    # When visiting first column and last column
    for r in range(ROWS):
        # DFS for first column for pacific
        visit_pac = dfs(r, 0, visit_pac, heights[r][0])
        # DFS for last column for atlantic
        visit_atl = dfs(r, COLS - 1, visit_atl, heights[r][COLS - 1])

    # Find intersection of both sets
    result = []
    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) in visit_atl and (row, col) in visit_pac:
                result.append([row, col])

    return result


if __name__ == "__main__":
    heights = []
    print(pacific_atlantic(heights))
