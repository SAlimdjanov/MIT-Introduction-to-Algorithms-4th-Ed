"""
heaps.py

"""

from math import floor


class Heap:
    """Heap class"""

    def __init__(self, heap):
        """Takes input array upon object initialization"""
        self.heap = heap

    def parent(self, index):
        """Returns the index of the parent node given an index of a child node"""
        return floor((index - 1) / 2) if index != 0 else 0

    def left_child(self, index):
        """Returns the index of the left child of a node at a given index"""
        return 2 * index + 1
        # return left if left < len(self.heap) else None

    def right_child(self, index):
        """Returns the index of the right child of a node at a given index"""
        return 2 * (index + 1)

    def validate_node(self, node_index):
        """Validate generated result"""
        return node_index if node_index < len(self.heap) else None


def main():
    """
    Main method

    """
    max_heap = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    my_max_heap = Heap(max_heap)
    size = len(max_heap)

    for x in range(0, size):
        parent_node = max_heap[my_max_heap.parent(x)]

        left = my_max_heap.left_child(x)
        right = my_max_heap.right_child(x)

        left_index = my_max_heap.validate_node(left)
        right_index = my_max_heap.validate_node(right)

        if left_index is not None:
            left_node = max_heap[left_index]
        else:
            left_node = "None"

        if right_index is not None:
            right_node = max_heap[right_index]
        else:
            right_node = "None"

        print(f"The parent of node {max_heap[x]} is {parent_node}")
        print(f"The left child of node {max_heap[x]} is {left_node}")
        print(f"The right child of node {max_heap[x]} is {right_node}")
        print("---")


if __name__ == "__main__":
    main()
