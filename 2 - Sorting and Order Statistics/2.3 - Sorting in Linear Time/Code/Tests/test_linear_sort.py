"""
test_linear_sort.py

"""

from copy import deepcopy
import numpy as np

from ..counting_sort import counting_sort
from ..bucket_sort import bucket_sort


def test_counting_sort():
    """Counting Sort Test (Without duplicate elements)"""
    array = [0, 2, 7, 3, 4, 6, 5, 1, 8]
    result = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert counting_sort(array, len(array), max(array)) == result


def test_counting_sort_duplicates():
    """Counting Sort Test (With duplicate elements)"""
    array = [6, 0, 2, 0, 1, 3, 4, 6, 3, 1, 2]
    result = [0, 0, 1, 1, 2, 2, 3, 3, 4, 6, 6]
    assert counting_sort(array, len(array), max(array)) == result


def test_bucket_sort():
    """Test counting sort"""
    test_data = list(np.random.default_rng().uniform(low=0.0, high=1.0, size=10))
    result = deepcopy(test_data)
    result.sort()
    assert bucket_sort(test_data, len(test_data)) == result
