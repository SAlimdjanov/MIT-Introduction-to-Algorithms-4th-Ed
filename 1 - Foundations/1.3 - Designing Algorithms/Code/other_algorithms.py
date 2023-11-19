"""
other_algorithms.py

Implementation of other algorithms covered in this section.

"""


def bubble_sort(array):
    """
    Bubble Sort Algorithm. Popular, but inefficent.

    Time complexity: O(n^2)
    Space complexity: O(1)

    Args:
        array (list[int]): Input array of integers
    """
    n = len(array)

    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]


def horner_rule(array, x):
    """
    Horner's rule for evaluating a polynomial P(x) = a_0 + a_1 * x + ... + a_n * x^n.

    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        array (list[int]): List of polynomial coefficents [a_0, a_1, ..., a_n]
        x (float): value of x

    Returns:
        float: Value of the polynomial equation at a given value of x
    """
    n, result = len(array), 0

    for i in range(n - 1, -1, -1):
        result = array[i] + x * result

    return result


def main():
    """
    Main method

    """
    array = [2, 4, 6, 7, 1, 2, 3, 5, 8, 10, 9]
    polynomial_coeff = [1, 2, 3, 0, 4]  # 1 + 2x + 3x^2 + 4x^4

    bubble_sort(array)
    print(array)

    p = horner_rule(polynomial_coeff, x=5)
    print(p)


if __name__ == "__main__":
    main()
