"""
test_heap_sort.py

"""

from copy import deepcopy
from ..heap_sort import HeapSort


max_heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

min_heap = deepcopy(max_heap)
min_heap.reverse()


def test_heap_sort_max():
    """Test Heap Sort Algorithm on a max-heap"""
    heap_sort_max = HeapSort(max_heap)
    heap_sort_max.heap_sort()

    expected_result = deepcopy(max_heap)
    expected_result.sort()

    assert heap_sort_max.heap == expected_result


def test_heap_sort_min():
    """Test Heap Sort Algorithm on a min-heap"""
    heap_sort_min = HeapSort(min_heap)
    heap_sort_min.heap_sort()

    expected_result = deepcopy(min_heap)
    expected_result.sort()

    assert heap_sort_min.heap == expected_result
