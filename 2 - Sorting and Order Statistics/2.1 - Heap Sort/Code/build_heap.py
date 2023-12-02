"""
build_heap.py

"""

from math import floor
from .heapify import Heapify


class BuildHeap(Heapify):
    """Build Max Heap Class"""

    def build_max_heap(self):
        """Construct a binary max heap"""
        for i in range(floor(self.heap_size / 2), -1, -1):
            self.max_heapify(i)

    def build_min_heap(self):
        """Construct a binary min heap"""
        for i in range(floor(self.heap_size / 2), -1, -1):
            self.min_heapify(i)
