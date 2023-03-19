from itertools import zip_longest as zipl


def is_matrix(matrix):
    return None not in sum(zipl(*matrix), ())


def are_compatible(matrix_A, matrix_B):
    num_entries = len(sum(matrix_A, [])) == len(sum(matrix_B, []))
    num_rows = len(matrix_A) == len(matrix_B)
    return all((num_entries, num_rows, is_matrix(matrix_A), is_matrix(matrix_B)))


def add(matrix_A, matrix_B):
    return [
        [sum(columns) for columns in zip(*rows)] for rows in zip(matrix_A, matrix_B)
    ]


def add2(matrix_A, matrix_B, dimensions):
    num_rows, num_columns = dimensions
    return [
        [matrix_A[i][j] + matrix_B[i][j] for i in range(num_rows)]
        for j in range(num_columns)
    ]
