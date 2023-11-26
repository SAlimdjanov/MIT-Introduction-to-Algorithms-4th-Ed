"""
heap_sort.py

"""

from build_heap import BuildHeap


class HeapSort(BuildHeap):
    """Heap Sort Class"""

    def __init__(self, heap):
        super().__init__(heap)
        self.n = self.heap_size - 1

    def heap_sort(self):
        """Heap Sort Algorithm

        Time complexity: O(n log n)
        Space complexity: O(1)
        """
        self.build_max_heap()

        for i in range(self.n, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heap_size -= 1
            self.max_heapify(0)


def main():
    """Main method"""
    input_array = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    heap_sort = HeapSort(input_array)

    heap_sort.heap_sort()
    print(heap_sort.heap)


if __name__ == "__main__":
    main()
