"""
insertion_sort_tests.py

"""


from copy import deepcopy

from ..insertion_sort import (
    insertion_sort,
    insertion_sort_reversed,
    binary_array_addition,
)

# Test data
sequence = [5, 2, 4, 6, 1, 3]
bin_a, bin_b = [1, 0, 1, 0], [1, 1, 1, 1]


def test_insertion_sort():
    """Insertion sort sorts correctly"""
    answer = deepcopy(sequence)
    answer.sort()

    result = insertion_sort(sequence, len(sequence))

    assert result == answer


def test_reversed_insertion_sort():
    """Reversed insertion sort sorts correctly"""
    answer = deepcopy(sequence)
    answer.sort()
    answer.reverse()

    result = insertion_sort_reversed(sequence, len(sequence))

    assert result == answer


def test_binary_array_addition():
    """Insertion sort sorts correctly"""
    answer = [1, 1, 0, 0, 1]
    result = binary_array_addition(bin_a, bin_b, len(bin_b))

    assert result == answer
