"""
test_linear_time_sort.py

"""

from copy import deepcopy
from random import randint

from numpy import random

from ..counting_sort import counting_sort
from ..bucket_sort import bucket_sort


def generate_result(input_array):
    """Generates sorted arrays for the unit tests below"""
    result = deepcopy(input_array)
    result.sort()

    return result


def test_counting_sort():
    """Counting Sort Test (without duplicate elements)"""
    array = [0, 2, 7, 3, 4, 6, 5, 1, 8]
    expected_result = generate_result(array)

    assert counting_sort(array, len(array), max(array)) == expected_result


def test_counting_sort_duplicates():
    """Counting Sort Test (with duplicate elements)"""
    array = [6, 0, 2, 0, 1, 3, 4, 6, 3, 1, 2]
    expected_result = generate_result(array)

    assert counting_sort(array, len(array), max(array)) == expected_result


def test_counting_sort_random():
    """Counting Sort Test (with randomly generated array)"""
    array = [randint(1, 10) for _ in range(randint(1, 10))]
    expected_result = generate_result(array)

    assert counting_sort(array, len(array), max(array)) == expected_result


def test_bucket_sort():
    """Test Bucket Sort"""
    array = [0.33, 0.27, 0.22, 0.17, 0.98, 0.75]
    expected_result = generate_result(array)

    assert bucket_sort(array, len(array)) == expected_result


def test_bucket_sort_random():
    """Test Bucket Sort (with randonly generated uniform distribution)"""
    test_data = list(random.default_rng().uniform(low=0.0, high=1.0, size=10))
    expected_result = generate_result(test_data)

    assert bucket_sort(test_data, len(test_data)) == expected_result
