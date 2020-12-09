def unique_paths(grid, rows, cols):
    if grid[0][0] == 1 or grid[rows][cols] == 1:
        # If start or destination cell is an obstacle
        return 0

    if rows == 0:
        # Only one way in the grid...so return one unique path
        left_terrain = [grid[0][i] for i in range(cols+1)]
        return 0 if any(left_terrain) else 1

    if cols == 0:
        left_terrain = [grid[i][0] for i in range(rows+1)]
        return 0 if any(left_terrain) else 1

    # Check for obstacles
    if grid[rows-1][cols] != 1 and grid[rows][cols-1] != 1:
        return unique_paths(grid, rows, cols-1) + unique_paths(grid, rows-1, cols)
    elif grid[rows-1][cols] == 1:
        return unique_paths(grid, rows, cols-1)
    elif grid[rows][cols-1] == 1:
        return unique_paths(grid, rows-1, cols)
    else:
        # The destination is blocked
        return 0


if __name__ == '__main__':
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    rows, cols = 3, 3
    print(unique_paths(grid, rows-1, cols-1))
