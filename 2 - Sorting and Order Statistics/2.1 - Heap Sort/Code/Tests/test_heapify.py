"""
test_heapify.py

"""

from ..heapify import Heapify


def is_max_heap(heap, heap_length):
    """Check if the given array represents a valid max-heap"""
    for i in range(heap_length):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        if left_child_index < heap_length and heap[i] < heap[left_child_index]:
            return False

        if right_child_index < heap_length and heap[i] < heap[right_child_index]:
            return False

    return True


def test_max_heapify():
    """Test max_heapify procedure on a violating max heap by calling it with the violating
    node's index"""
    max_array = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heapify_max = Heapify(max_array)
    heapify_max.max_heapify(1)

    assert is_max_heap(heapify_max.heap, heapify_max.heap_size)


def is_min_heap(heap, heap_length):
    """Check if the given array represents a valid min-heap"""
    for i in range(heap_length):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        if left_child_index < heap_length and heap[i] > heap[left_child_index]:
            return False

        if right_child_index < heap_length and heap[i] > heap[right_child_index]:
            return False

    return True


def test_min_heapify():
    """Test min_heapify procedure on a violating min heap by calling it with the violating
    node's index"""
    min_array = [1, 3, 14, 4, 7, 8, 9, 5, 10, 16]
    heapify_min = Heapify(min_array)
    heapify_min.min_heapify(2)

    assert is_min_heap(heapify_min.heap, heapify_min.heap_size)
