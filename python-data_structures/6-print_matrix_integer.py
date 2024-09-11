#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Format each integer in the row and join them with a space
        print(' '.join('{:d}'.format(num) for num in row)
