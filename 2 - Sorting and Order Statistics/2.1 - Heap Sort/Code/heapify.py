"""
heapify.py

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
        left_child = self.left_child(index)
        right_child = self.right_child(index)

        # Note: Beware of pseudocode, '<' replaced '<=' due to the arrays being 0-indexed

        if left_child < self.heap_size and self.heap[left_child] > self.heap[index]:
            largest = left_child
        else:
            largest = index

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

        if left_child < self.heap_size and self.heap[left_child] < self.heap[index]:
            smallest = left_child
        else:
            smallest = index

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


def main():
    """
    Main method

    """
    max_array = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heapify_max = Heapify(max_array)

    # Choose index 1, as that is the violating node
    heapify_max.max_heapify(1)
    print(heapify_max.heap)

    min_array = [1, 3, 14, 4, 7, 8, 9, 2, 10, 16]
    heapify_min = Heapify(min_array)

    # Choose the violating node (index 2)
    heapify_min.min_heapify(2)
    print(heapify_min.heap)


if __name__ == "__main__":
    main()
