"""
matrix_multiply.py

"""


def matrix_multiply_naive(a, b, c, n):
    """Naive implementation of matrix multiplication

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


def print_matrix(matrix):
    """Print matrix rows"""
    for row in matrix:
        print(row)


def main():
    """
    Main method

    """
    matrix_a = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    matrix_b = [[16, 17, 18, 19], [20, 21, 22, 23], [24, 25, 26, 27], [28, 29, 30, 31]]
    matrix_c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    matrix_multiply_naive(matrix_a, matrix_b, matrix_c, len(matrix_c))
    print("---Naive---")
    print_matrix(matrix_c)

    matrix_c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    matrix_multiply_recursive(matrix_a, matrix_b, matrix_c, len(matrix_c))
    print("---Recursive---")
    print_matrix(matrix_c)


if __name__ == "__main__":
    main()
