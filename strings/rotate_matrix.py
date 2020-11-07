import random

def display_matrix(matrix):
    for row in matrix:
        print(row)

def rotate_matrix(matrix):
    mat_len = len(matrix)
    new_matrix = [[] for i in range(mat_len)]
    for i in reversed(range(mat_len)):
        for j in range(mat_len):
            new_matrix[j].append(matrix[i][j])

    return new_matrix
        


if __name__ == '__main__':
    N = 5
    matrix = [random.sample(range(1, 99), N) for _ in range(N)]
    print('Original:')
    display_matrix(matrix)
    print('Rotated')
    display_matrix(rotate_matrix(matrix))