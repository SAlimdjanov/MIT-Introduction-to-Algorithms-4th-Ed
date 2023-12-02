"""
test_divide_and_conquer.py

"""


from copy import deepcopy

from ..bubble_sort import bubble_sort
from ..horners_rule import horners_rule
from ..merge_sort import merge_sort


def test_bubble_sort():
    """bubble_sort sorts correctly"""
    array = [2, 4, 6, 7, 1, 2, 3, 5, 8, 10, 9]
    bubble_sort(array)

    sorted_array = deepcopy(array)
    sorted_array.sort()

    assert array == sorted_array


def test_horners_rule():
    """horners_rule evaluates the polynomial correctly"""
    polynomial_coeff = [1, 2, 3, 0, 4]  # p(x) =  1 + 2x + 3x^2 + 4x^4
    answer = 2586

    p = horners_rule(polynomial_coeff, x=5)

    assert p == answer


def test_merge_sort():
    """merge_sort sorts correctly"""
    array = [2, 4, 6, 7, 1, 2, 3, 5]

    sorted_array = deepcopy(array)
    sorted_array.sort()

    merge_sort(array, 0, 7)

    assert array == sorted_array
