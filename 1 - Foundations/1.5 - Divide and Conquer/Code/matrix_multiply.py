"""
matrix_multiply.py

"""


def matrix_multiply_iterative(a, b, c, n):
    """Iterative implementation of matrix multiplication

    Time complexity: O(n^3)
    Space complexity: O(1)

    Args:
        A (2D list): Matrix A
        B (2D list): Matrix B
        C (2D list): Matrix C (Matrix of 0s)
        n (int): Dimension of the square matrices
    """
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]


def matrix_multiply_recursive(a, b, c, n):
    """The divide-and-conquer (recursive) implementation of matrix multiplication

    Time complexity: O(n^3)
    Space complexity: O(n log(n))

    Args:
        A (2D list): Matrix A
        B (2D list): Matrix B
        C (2D list): Matrix C (Matrix of 0s)
        n (int): Dimension of the square matrices
    """
    if n == 1:
        c[0][0] = c[0][0] + a[0][0] * b[0][0]
        return

    a11, a12, a21, a22 = (
        [row[: n // 2] for row in a[: n // 2]],
        [row[n // 2 :] for row in a[: n // 2]],
        [row[: n // 2] for row in a[n // 2 :]],
        [row[n // 2 :] for row in a[n // 2 :]],
    )

    b11, b12, b21, b22 = (
        [row[: n // 2] for row in b[: n // 2]],
        [row[n // 2 :] for row in b[: n // 2]],
        [row[: n // 2] for row in b[n // 2 :]],
        [row[n // 2 :] for row in b[n // 2 :]],
    )

    c11, c12, c21, c22 = (
        [row[: n // 2] for row in c[: n // 2]],
        [row[n // 2 :] for row in c[: n // 2]],
        [row[: n // 2] for row in c[n // 2 :]],
        [row[n // 2 :] for row in c[n // 2 :]],
    )

    matrix_multiply_recursive(a11, b11, c11, n // 2)
    matrix_multiply_recursive(a12, b21, c11, n // 2)
    matrix_multiply_recursive(a11, b12, c12, n // 2)
    matrix_multiply_recursive(a12, b22, c12, n // 2)
    matrix_multiply_recursive(a21, b11, c21, n // 2)
    matrix_multiply_recursive(a22, b21, c21, n // 2)
    matrix_multiply_recursive(a21, b12, c22, n // 2)
    matrix_multiply_recursive(a22, b22, c22, n // 2)

    for i in range(n // 2):
        for j in range(n // 2):
            c[i][j] = c11[i][j]
            c[i][j + n // 2] = c12[i][j]
            c[i + n // 2][j] = c21[i][j]
            c[i + n // 2][j + n // 2] = c22[i][j]
