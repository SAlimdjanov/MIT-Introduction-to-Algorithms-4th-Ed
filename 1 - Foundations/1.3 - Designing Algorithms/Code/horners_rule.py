"""
horners_rule.py

"""


def horners_rule(coeff, x):
    """Horner's rule for evaluating a polynomial of the form P(x) = a_0 + a_1 * x + ... + a_n * x^n.

    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        coeff (list[int]): List of polynomial coefficents [a_0, a_1, ..., a_n]
        x (float): value of x

    Returns:
        float: Value of the polynomial equation at a given value of x
    """
    n, result = len(coeff), 0

    for i in range(n - 1, -1, -1):
        result = coeff[i] + x * result

    return result
