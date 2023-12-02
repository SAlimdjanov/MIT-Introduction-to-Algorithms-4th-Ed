"""
test_build_heap.py

"""

from ..build_heap import BuildHeap
from .test_heapify import is_max_heap, is_min_heap


array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]


def test_build_max_heap():
    """Method build_max_heap constructs a valid max-heap"""
    max_heap = BuildHeap(array)
    max_heap.build_max_heap()

    assert is_max_heap(max_heap.heap, max_heap.heap_size)


def test_build_min_heap():
    """Method build_min_heap constructs a valid min-heap"""
    min_heap = BuildHeap(array)
    min_heap.build_min_heap()

    assert is_min_heap(min_heap.heap, min_heap.heap_size)
