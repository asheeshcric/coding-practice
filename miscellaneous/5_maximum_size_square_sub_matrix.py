def max_sub_matrix(matrix, rows, cols):
    temp = [[0 for _ in range(cols)] for _ in range(rows)]

    # Copy the first row and col from the original matrix
    for row in range(rows):
        temp[row][0] = matrix[row][0]

    for col in range(cols):
        temp[0][col] = matrix[0][col]

    max_size = 0
    for row in range(1, rows):
        for col in range(1, cols):
            if matrix[row][col] == 1:
                # Find the min(left-top, min(left, top)) + 1
                temp[row][col] = min(temp[row-1][col-1],
                                     min(temp[row-1][col], temp[row][col-1])) + 1

                max_size = max(max_size, temp[row][col])
            else:
                temp[row][col] = 0


    return max_size
