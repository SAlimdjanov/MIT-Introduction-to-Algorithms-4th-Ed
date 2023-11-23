"""
max_heapify.py

"""

from heaps import Heap


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
        left = self.left_child(index)
        right = self.right_child(index)

        if left <= self.heap_size and self.heap[left] > self.heap[index]:
            largest = left
        else:
            largest = index

        if right <= self.heap_size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest)


def main():
    """
    Main method

    """
    array = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heapify = Heapify(array)

    # Choose index 1, as that is the violating node
    heapify.max_heapify(1)
    print(heapify.heap)


if __name__ == "__main__":
    main()
