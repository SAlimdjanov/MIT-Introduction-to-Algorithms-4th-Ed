"""
heapify.py

"""

from .heaps import Heap


class Heapify(Heap):
    """Heapify class"""

    def __init__(self, heap):
        super().__init__(heap)
        # For now, assume all elements in the array are part of the heap
        self.heap_size = len(heap)

    def max_heapify(self, index):
        """Converts a heap that violates the max-heap property into a valid binary heap

        Time complexity: O(log n)
        Space complexity: O(log n)

        Args:
            heap (list[int]): Input binary heap
            index (int): Starting index
        """
        left_child = self.left_child(index)
        right_child = self.right_child(index)

        largest = index

        if left_child < self.heap_size and self.heap[left_child] > self.heap[index]:
            largest = left_child

        if right_child < self.heap_size and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest)

    def min_heapify(self, index):
        """Converts a heap into a minimum binary heap in an analogous manner to that of the
        procedure above"""
        left_child = self.left_child(index)
        right_child = self.right_child(index)

        smallest = index

        if left_child < self.heap_size and self.heap[left_child] < self.heap[index]:
            smallest = left_child

        if (
            right_child < self.heap_size
            and self.heap[right_child] < self.heap[smallest]
        ):
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self.min_heapify(smallest)
