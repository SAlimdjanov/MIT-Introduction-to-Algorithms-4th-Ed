"""
test_quicksort.py

"""

from copy import deepcopy
from random import randrange

from ..quicksort import Quicksort
from ..randomized_quicksort import RandomizedQuicksort


def test_quicksort():
    """Test Quicksort"""
    array = [2, 8, 7, 1, 3, 5, 6, 4]
    p = 0
    r = len(array) - 1

    expected_result = deepcopy(array)
    expected_result.sort()

    quicksort = Quicksort(array)
    quicksort.quicksort(p, r)

    assert quicksort.array == expected_result


def test_quicksort_random():
    """Test Quicksort (with randomly generated array)"""
    array = [randrange(1, 10) for _ in range(randrange(1, 10))]
    p = 0
    r = len(array) - 1

    expected_result = deepcopy(array)
    expected_result.sort()

    quicksort = Quicksort(array)
    quicksort.quicksort(p, r)

    assert quicksort.array == expected_result


def test_randomized_quicksort():
    """Test Randomized Quicksort"""
    array = [2, 8, 7, 1, 10, 5, 6, 4, 9, 3]
    p = 0
    r = len(array) - 1

    expected_result = deepcopy(array)
    expected_result.sort()

    quicksort = RandomizedQuicksort(array)
    quicksort.randomized_quicksort(p, r)

    assert quicksort.array == expected_result


def test_randomized_quicksort_random():
    """Test Randomized Quicksort (with randomly generated array)"""
    array = [randrange(1, 10) for _ in range(randrange(1, 10))]
    p = 0
    r = len(array) - 1

    expected_result = deepcopy(array)
    expected_result.sort()

    quicksort = RandomizedQuicksort(array)
    quicksort.randomized_quicksort(p, r)

    assert quicksort.array == expected_result
