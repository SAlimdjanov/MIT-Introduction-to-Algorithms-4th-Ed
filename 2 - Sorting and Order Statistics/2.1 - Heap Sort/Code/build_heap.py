"""
build_heap.py

"""

from math import floor
from heapify import Heapify


class ConstructMaxHeap(Heapify):
    """Build Max Heap Class"""

    def build_max_heap(self):
        """Construct a binary max heap"""
        for i in range(floor(self.heap_size / 2), -1, -1):
            self.max_heapify(i)

    def build_min_heap(self):
        """Construct a binary min heap"""
        for i in range(floor(self.heap_size / 2), -1, -1):
            self.min_heapify(i)


def main():
    """Main method"""
    array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

    construct_max_heap = ConstructMaxHeap(array)
    construct_max_heap.build_max_heap()
    print(construct_max_heap.heap)

    construct_min_heap = ConstructMaxHeap(array)
    construct_min_heap.build_min_heap()
    print(construct_min_heap.heap)


if __name__ == "__main__":
    main()
