"""
test_matrix_multiply.py

"""

from ..matrix_multiply import matrix_multiply_iterative, matrix_multiply_recursive

# Matrices
matrix_a = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
matrix_b = [[16, 17, 18, 19], [20, 21, 22, 23], [24, 25, 26, 27], [28, 29, 30, 31]]
matrix_c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Solution
answer = [
    [152, 158, 164, 170],
    [504, 526, 548, 570],
    [856, 894, 932, 970],
    [1208, 1262, 1316, 1370],
]


def test_iterative():
    """Confirm that the iterative method produces the correct answer"""
    matrix_multiply_iterative(matrix_a, matrix_b, matrix_c, len(matrix_c))

    assert matrix_c == answer


def test_recursive():
    """Confirm that the recursive method produces the correct answer"""

    # Re-initialize destination matrix before running second test
    new_matrix_c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    matrix_multiply_recursive(matrix_a, matrix_b, new_matrix_c, len(new_matrix_c))

    assert new_matrix_c == answer
