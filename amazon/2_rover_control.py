# Input
n = 4
cmds = ['RIGHT', 'UP', 'DOWN', 'LEFT', 'DOWN', 'DOWN']

move_map = {'RIGHT': (0, 1), 'LEFT': (0, -1), 'UP': (-1, 0), 'DOWN': (1, 0)}


def get_pos(curr_row, curr_col):
    return curr_row*n + curr_col
    


# Current position (starts at position 0)
row, col = 0, 0
# Calculate the position boundaries (pos should be between these boundaries)
min_pos = 0
max_pos = n*n - 1
for cmd in cmds:
    row_step, col_step = move_map[cmd]
    # Check if the new position is valid or not
    curr_pos = get_pos(row+row_step, col+col_step)
    if curr_pos >= min_pos and curr_pos <= max_pos:
        row += row_step
        col += col_step

print(get_pos(row, col))


