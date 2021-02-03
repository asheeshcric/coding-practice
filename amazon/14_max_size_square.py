def largest_size(matrix, rows, cols):
    temp = [[0 for _ in range(cols)] for _ in range(rows)]

    # Copy the first row and col from the matrix
    for row in range(rows):
        temp[row][0] = matrix[row][0]

    for col in range(cols):
        temp[0][col] = matrix[0][col]

    max_size = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                temp[row][col] = min(
                    temp[row-1][col-1], min(temp[row][col-1], temp[row-1][col])
                ) + 1

                max_size = max(temp[row][col], max_size)
            else:
                temp[row][col] = 0


    return max_size